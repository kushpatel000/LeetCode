#!/bin/python3

import requests
import datetime
from pathlib import Path
import json
from bs4 import BeautifulSoup
import textwrap
import re
import subprocess, shutil

URL = 'https://leetcode.com/graphql'
HEADERS = {
    'Content-Type':'application/json',
    'Referer':'https://leetcode.com'
}


QUERY_GETDAILYPROBLEMNUMBER = '''
query getDailyProblem {
    activeDailyCodingChallengeQuestion {
        question {
            questionFrontendId
        }
    }
}
'''

    
QUERY_GETDAILYPROBLEM = '''
query getDailyProblem {
    activeDailyCodingChallengeQuestion {
        date
        link
        question {
            questionFrontendId
            title
            titleSlug
            difficulty
            content

            exampleTestcaseList
            
            codeSnippets {
                lang
                langSlug
                code
            }
        }

    }
}
'''

QUERY_GETPROBLEMBYNUMBER = '''
query getProblemSlug($search: String) {
  problemsetQuestionList: questionList(
    categorySlug: ""
    limit: 1
    skip: 0
    filters: { searchKeywords: $search }
  ) {
    questions: data {
      questionFrontendId
      title
      titleSlug
      difficulty
      content

      exampleTestcaseList

      codeSnippets {
        lang
        langSlug
        code
      }
    }
  }
}
'''


def send_leetcode_request(query:str|dict) -> requests.Response:
    if isinstance(query, str):
        payload = {'query':query}
    elif isinstance(query, dict):
        payload = query
    else:
        raise ValueError(f'Expected `query` as type str or dict, got `{type(query)}`')


    resp = requests.post(
        url=URL,
        headers=HEADERS,
        json=payload,
    )
    resp.raise_for_status()

    return resp


def get_problem_number() -> int:
    resp = send_leetcode_request(QUERY_GETDAILYPROBLEMNUMBER)
    qid = (
        resp.json() 
            .get('data',{})
            .get('activeDailyCodingChallengeQuestion',{})
            .get('question',{})
            .get('questionFrontendId','-1')
    )
    # print(json.dumps(resp.json(), indent=2))
    qid = int(qid)
    if qid == -1: raise ValueError('`get_problem_number` - issue parsing data')

    return qid


def check_exists(qid:int) -> bool:
    loc = Path.cwd()
    test_loc = Path.cwd() / 'Test_Cases'
    py_match = list( loc.glob(f'p{qid:04d}*.py') )
    test_match = list( test_loc.glob(f'p{qid:04d}*.json') )

    flag = False
    if py_match: 
        print('Python file found')
        flag = True
    if test_match:
        print('Test cases file found')
        flag = True
    
    return flag


def _clean_content(content_html:str) -> str:
    soup = BeautifulSoup(content_html, 'html.parser')
    for sup in soup.find_all('sup'):
        sup.replace_with( f'^{sup.text}' )

    content_str = soup.text
    content_str_wrapped = []
    for line in content_str.split('\n'):
        wrapped_ = [f'#  {wline}' for wline in textwrap.wrap(line, width=80)]
        content_str_wrapped.extend(wrapped_)

    return '\n'.join(content_str_wrapped)


def export_python_snippet(qdata:dict) -> None:
    code_snippets = qdata.get('codeSnippets')

    python_snippet = ''
    for cs in code_snippets:
        if cs.get('langSlug') == 'python3':
            python_snippet = cs.get('code')
        elif cs.get('langSlug') == 'python' and python_snippet == '':
            python_snippet = cs.get('code')

    try:
        function_name = re.search(
            pattern=r'def (.*)\(',
            string=python_snippet
        ).group(1)
    except Exception as e:
        print(f'Caught exception {type(e)} {e}')
        function_name = 'XXXXXX'


    problem_number  = int(qdata.get('questionFrontendId'))
    problem_title   = qdata.get('title')
    problem_diff    = qdata.get('difficulty')
    problem_content = _clean_content(qdata.get('content'))
    problem_link    = f'https://leetcode.com/problems/{qdata.get('titleSlug')}'

    python_code_sugar = f'''
# {problem_number:04d}. {problem_title} [{problem_diff}]
# {problem_link} 

{problem_content}

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

{python_snippet}



if __name__ == '__main__':
    print('\\n'*10)


    sol = Solution()

    test_funcs = [
        sol.{function_name}
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

    '''.strip()


    python_file = Path.cwd() / f'p{problem_number:04d}.py'
    assert not python_file.exists(), 'Python file exists, delete to overwrite'
    python_file.write_text(python_code_sugar)
    print(f'Exported to:')
    print(f'  {python_file}')
    
    return python_file


def export_test_cases(qdata:dict) -> None:

    problem_number = int(qdata.get('questionFrontendId'))
    test_file = Path.cwd() / f'Test_Cases/p{problem_number:04d}.json'
    assert not test_file.exists(), 'Test file exists, delete to overwrite'

    test_cases = list()
    for ex in qdata.get('exampleTestcaseList'):
        case = [
            eval(ex.replace('\n', ',')),
            None # outputs to be filled in later
        ]
        test_cases.append(case)

    test_file.write_text(json.dumps(test_cases, indent=4))
    return test_file



def get_todays_problem() -> tuple[str, dict]:
    resp = send_leetcode_request(QUERY_GETDAILYPROBLEM)
    data = resp.json().get('data',{}).get('activeDailyCodingChallengeQuestion')
    assert data is not None, '`get_todays_problem` - No results found'

    link = f'https://leetcode.com' + data.get('link')
    qdata = data.get('question')
    assert qdata is not None, '`get_todays_problem` - No question data'
    
    return link, qdata


def get_problem_by_number(number:int) -> tuple[str, dict]:
    resp = send_leetcode_request({
        'query': QUERY_GETPROBLEMBYNUMBER,
        'variables': {'search':str(number)}
    })
    data = (
        resp.json()
            .get('data',{})
            .get('problemsetQuestionList',{})
            .get('questions',[])
    )

    if len(data) == 0:
        raise ValueError(f'No result found for Problem {number}.')
    elif len(data) > 1:
        print(f'search: {number}')
        print('found:')
        for q in data:
            qid = data.get('questionFrontendId')
            ttl = data.get('title')
            print(f' - {qid:4s}. {ttl}')
        raise ValueError(f'Multiple results found for Problem {number}.')

    question_data = data[0]
    return question_data

def download_and_export_problem(qid:str):
    if qid.isnumeric():
        qid = int(qid)
    else:
        qid = get_problem_number()

    # check if it already exists
    check = check_exists(qid)

    if check:
        print(f'Problem number {qid} already downloaded.')
        return

    # if not, pull it
    print(f'Pulling problem number {qid}...')

    question_data = get_problem_by_number(qid)

    # export the information
    py_file = export_python_snippet(question_data)    
    test_file = export_test_cases(question_data)

    # open the files in VS Code
    cmd = shutil.which('code')
    if cmd:
        subprocess.run([cmd, py_file, test_file])
    else:
        print('Cannot find `code` command.')



def main():
    download_and_export_problem()


if __name__ == '__main__':
    # get_problem_by_number(1)
    main()
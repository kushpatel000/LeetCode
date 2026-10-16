#!/bin/python3

import requests
import datetime
from pathlib import Path
import json

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


def send_leetcode_request(query:str) -> requests.Response:
    resp = requests.post(
        url=URL,
        headers=HEADERS,
        json={'query':query},
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


def export_python_snippet(qdata:dict, link:str) -> None:
    code_snippets = qdata.get('codeSnippets')

    python_snippet = ''
    for cs in code_snippets:
        if cs.get('langSlug') == 'python3':
            python_snippet = cs.get('code')
        elif cs.get('langSlug') == 'python' and python_snippet == '':
            python_snippet = cs.get('code')

    problem_number = int(qdata.get('questionFrontendId'))
    problem_title  = qdata.get('title')
    problem_diff   = qdata.get('difficulty')

    python_code_sugar = f'''
# {problem_number:04d}. {problem_title} [{problem_diff}]
# {link} 

from typing import List
import test_suite as ts

{python_snippet}



if __name__ == '__main__':
    print('\\n'*10)


    sol = Solution()

    test_funcs = [
        
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



def export_test_cases(qdata:dict) -> None:

    problem_number = int(qdata.get('questionFrontendId'))
    test_file = Path.cwd() / f'Test_Cases/p{problem_number:04d}.json'
    assert not test_file.exists(), 'Test file exists, delete to overwrite'

    test_cases = list()
    for ex in qdata.get('exampleTestcaseList'):
        case = [
            eval(ex),
            None # outputs to be filled in later
        ]
        test_cases.append(case)

    test_file.write_text(json.dumps(test_cases, indent=4))



def get_todays_problem() -> tuple[str, dict]:
    resp = send_leetcode_request(QUERY_GETDAILYPROBLEM)
    data = resp.json().get('data',{}).get('activeDailyCodingChallengeQuestion')
    assert data is not None, '`get_todays_problem` - No results found'

    link = f'https://leetcode.com' + data.get('link')
    qdata = data.get('question')
    assert qdata is not None, '`get_todays_problem` - No question data'
    
    
    return link, qdata





def main():
    # get today's problem number
    qid = get_problem_number()

    # check if it already exists
    check = check_exists(qid)

    if check:
        print(f'Problem number {qid} already downloaded.')
        return

    # if not, pull it
    print(f'Pulling problem number {qid}...')

    link, question = get_todays_problem()

    export_python_snippet(question, link)    
    export_test_cases(question)



if __name__ == main():
    main()
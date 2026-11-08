# 0022. Generate Parentheses

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def traverse(curr:str, depth:int):
            if len(curr) == 2*n:
                result.append(curr)
                return

            if depth + len(curr) == 2*n:
                result.append(curr + ')' * depth)
                return
            
            if depth < n:
                traverse(curr+'(', depth+1)
            if depth > 0:
                traverse(curr+')', depth-1)

        traverse('', 0)
        return result

    def generateParenthesis_v2(self, n: int) -> List[str]:
        result = []

        def traverse(curr:str, depth:int):
            if depth + len(curr) == 2*n:
                result.append(curr + ')' * depth)
                return
            
            if depth < n:
                traverse(curr+'(', depth+1)
            if depth > 0:
                traverse(curr+')', depth-1)

        traverse('', 0)
        return result


if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.generateParenthesis,
        sol.generateParenthesis_v2
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )


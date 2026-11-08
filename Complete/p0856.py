# 0856. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def scoreOfParentheses_recurse(self, s: str) -> int:
        if s == '()': return 1

        score = 0

        d = 0
        curr_open = None
        for i,c in enumerate(s):
            if d == 0 and c == '(':
                curr_open = i

            d += 1 if c == '(' else -1

            if d == 0 and c == ')':
                if i - curr_open == 1:
                    score += 1
                else:
                    sub_score = self.scoreOfParentheses_recurse( s[curr_open+1:i] )
                    score += 2*sub_score

        return score
            
    def scoreOfParentheses_stack(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == '(':
                stack.append(0)
            else:
                val = max(2*stack.pop(), 1)
                stack[-1] += val

        return stack[0]
                             



if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.scoreOfParentheses_recurse,
        sol.scoreOfParentheses_stack
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )


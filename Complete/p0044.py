# 0044. Wildcard Matching

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        len(s) >= len(p)
        '''
        def traverse(i:int, j:int) -> bool:
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if i == len(s):
                return all(p[k] == '*' for k in range(j, len(p)))

            # print(f's[{i}] = {s[i] if i < len(s) else None}, p[{j}] = {p[j]}')

            # question mark check
            if p[j] == '?':
                return traverse(i+1, j+1)

            # asterisk check
            if p[j] == '*':
                # check if next char is *, if so, skip this one
                if p[j+1:j+2] == '*':
                    return traverse(i, j+1)

                check0 = traverse(i,j+1)    # no match
                check1 = traverse(i+1,j)    # curr char match, use * for next
                checkn = traverse(i+1,j+1)  # everything after *
                return check0 or check1 or checkn

            # standard character check
            if s[i] == p[j]:
                return traverse(i+1, j+1)
        
            return False
        
        return traverse(0,0)

    def isMatch_v2(self, s: str, p: str) -> bool:
        '''
        len(s) >= len(p)
        '''
        @cache
        def traverse(i:int, j:int) -> bool:
            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if i == len(s):
                return all(p[k] == '*' for k in range(j, len(p)))

            # print(f's[{i}] = {s[i] if i < len(s) else None}, p[{j}] = {p[j]}')

            # question mark check
            if p[j] == '?':
                return traverse(i+1, j+1)

            # asterisk check
            if p[j] == '*':
                # check if next char is *, if so, skip this one
                if p[j+1:j+2] == '*':
                    return traverse(i, j+1)

                # truncates recursion tree early
                return traverse(i,j+1) or traverse(i+1,j) or traverse(i+1,j+1)
                # check0 = traverse(i,j+1)    # no match
                # check1 = traverse(i+1,j)    # curr char match, use * for next
                # checkn = traverse(i+1,j+1)  # everything after *
                # return check0 or check1 or checkn

            # standard character check
            if s[i] == p[j]:
                return traverse(i+1, j+1)
        
            return False

        # first and last character checks
        if p and s and p[0] not in '?*' and p[0] != s[0]:
            return False
        if p and s and p[-1] not in '?*' and p[-1] != s[-1]:
            return False
        
        return traverse(0,0)

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        # sol.isMatch,
        sol.isMatch_v2
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


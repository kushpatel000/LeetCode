# 0678. Valid Parenthesis String

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def __init__(self):
        self.cases = dict()

    def checkValidString_recursion(self, s: str) -> bool:
        while '()' in s:
            s = s.replace('()','')

        l = s.count('(')
        r = s.count(')')
        a = s.count('*')
        # print(f'{l=}, {r=}, {a=}')

        if abs(l-r) > a: return False
        # print('proceding to dfs')

        @cache
        def dfs(i:int, depth:int) -> bool:
            # self.cases[(i,depth)] = self.cases.get((i,depth), 0) + 1

            if depth < 0:
                # print('Negative depth')
                return False

            if i == len(s):
                # print('End of string')
                return depth == 0
            
            if len(s) - i < depth: 
                # print('Insufficient characters left to balance')
                return False
            
            if s[i] == '(':
                return dfs(i+1, depth+1)
            elif s[i] == ')':
                return dfs(i+1, depth-1)
            else: # asterisk
                return dfs(i+1, depth) \
                    or dfs(i+1, depth+1) \
                    or dfs(i+1, depth-1) \

        
        return dfs(0,0)

    def checkValidString_opts(self, s: str) -> bool:
        prev_set = {0}
        for c in s:
            curr_set = set()
            for depth in prev_set:
                if c == '(':
                    curr_set.add(depth+1)
                elif c == ')':
                    if depth > 0:
                        curr_set.add(depth-1)
                else: # asterisk
                    curr_set.add(depth)
                    curr_set.add(depth+1)
                    if depth > 0:
                        curr_set.add(depth-1)
            prev_set = curr_set
        return 0 in prev_set
    

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.checkValidString_recursion,
        sol.checkValidString_opts
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # for k,v in sol.cases.items():
    #     i,d = k
    #     print(f'{i:3d} {d:3d}: {v:5d}')


# [
#     "**************************************************))))))))))))))))))))))))))))))))))))))))))))))))))",
#     true
# ]
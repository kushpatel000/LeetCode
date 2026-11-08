
# 1807. Evaluate the Bracket Pairs of a String

from functools import cache
from typing import List
import test_suite as ts


class Solution:
        
    def evaluate_jloop(self, packet:list) -> str:
        s, knowledge = packet

        kv = dict(knowledge)
    
        res = list()
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = i+1
                while s[j] != ')': j += 1
                res.append( kv.get(s[i+1:j], '?') )
                i = j+1

            else:
                res.append(s[i])
                i += 1

        return ''.join(res)

    def evaluate_find(self, packet:list) -> str:
        s, knowledge = packet

        kv = dict(knowledge)
    
        res = list()
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = s.find(')', i+1) 
                res.append( kv.get(s[i+1:j], '?') )
                i = j+1

            else:
                res.append(s[i])
                i += 1

        return ''.join(res)
        
if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.evaluate_jloop,
        sol.evaluate_find,
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # for i, tc in enumerate(test_cases):
    #     res = sol.maxDepthAfterSplit( tc[0] )
    #     print(res)

    #     print(f'== Test Case {i} ==')
    #     print('My Solution')
    #     sol.show_depths(tc[0], res)
        
    #     print('\nKey')
    #     sol.show_depths(tc[0], tc[1])
        
    #     print()
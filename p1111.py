
# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

from functools import cache
from typing import List
import test_suite as ts


class Solution:
    def calc_max_depth(self, seq:str) -> int:
        cd = 0
        md = 0

        for c in seq:
            if c == '(':
                cd += 1
                md = max(md, cd)
            else:
                cd -= 1
        return md

    def show_depths(self, seq:str, choice:list) -> None:
        strings = ['','']
        for c, a in zip(seq, choice):
            strings[a] += c

        for s in strings:
            md = self.calc_max_depth(s)
            print(f'{md:2d} {s}')

    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        '''
        Greedily choose 0 or 1 such that the sum(0) >= sum(1)
        but that the difference is minimized.
        '''

        pts = [0, 0]
        choice = list()

        for c in seq:
            if c == '(':
                i = 0 if pts[0]==pts[1] else 1
                pts[i] += 1
                choice.append(i)
            else:
                i = 1 if pts[0]==pts[1] else 0
                pts[i] -= 1
                choice.append(i)
        
        return choice

    def maxDepthAfterSplit_v2(self, seq: str) -> list[int]:
        '''
        Greedily choose 0 or 1 such that the sum(0) >= sum(1)
        but that the difference is minimized.
        '''

        delta = 0
        choice = list()

        opts = {
            ('(', True) : (0, 1),
            ('(', False) : (1, -1),
            (')', True) : (1, 1),
            (')', False) : (0, -1)
        }

        for c in seq:
            i, d = opts[( c, delta==0 )]
            choice.append(i)
            delta += d
        
        return choice
    
    def maxDepthAfterSplit_cheat(self, seq: str) -> list[int]:
        '''
        Greedily choose 0 or 1 such that the sum(0) >= sum(1)
        but that the difference is minimized.
        '''

        depth = 0
        choice = [0] * len(seq)

        for i,c in enumerate(seq):
            if c == '(':
                depth += 1
                choice[i] = depth%2
            else:
                choice[i] = depth%2
                depth -= 1
            
        return choice



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.maxDepthAfterSplit,
        sol.maxDepthAfterSplit_v2,
        sol.maxDepthAfterSplit_cheat
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        check_thresh = 1e-5,
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
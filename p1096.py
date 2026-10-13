
# 1096. Brace Expansion II

from functools import cache
from typing import List
import test_suite as ts


class Solution:
    def find_pair(self, s:str, start:int) -> int:
        d = 0
        i = start
        while i < len(s):
            if s[i] == '{':
                d += 1
            elif s[i] == '}':
                d -= 1
                if d == 0: return i
            i += 1
        return len(s)

    def split_comma(self, s:str) -> list[str]:
        depth  = 0
        splits = list()

        last_comma = -1
        for i,c in enumerate(s):
            if c == '{':
                depth += 1
            elif c =='}':
                depth -= 1
            elif c == ',' and depth == 0:
                splits.append( s[last_comma+1:i] )
                last_comma = i

        if depth == 0:
            splits.append( s[last_comma+1:] )
        return splits


    def braceExpansionII_recurse(self, expression: str) -> list[str]:
        if '{' not in expression: return [expression]

        pieces = ['']
        
        i = 0
        while i < len(expression):
            c = expression[i]
            # print(i,c, expression[i:])

            if c == '}':
                print('hit }')
                i += 1
            elif c == '{':
                j = self.find_pair( expression, i )
                splits = self.split_comma(expression[i+1:j])
                # print( 'test', expression[i:j+1] )
                # print( 'test-', expression[i+1:j] )
                # print( 'split', splits)

                pieces = [p+spl for spl in splits for p in pieces]

                i = j+1
            else:
                pieces = [ p+c for p in pieces ]
                i += 1
            # print(f'end {i=}')

        res = list()
        for p in pieces:
            if '{' in p:
                res.extend(self.braceExpansionII_recurse(p))
            else:
                res.append(p)
        

        return sorted(set(res))



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.braceExpansionII_recurse,
        
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
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
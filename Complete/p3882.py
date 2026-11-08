# 3882. Minimum XOR Path in a Grid [Medium]
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/ 

from typing import List
import test_suite as ts

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        MAX = 2**10
        R, C = len(grid), len(grid[0])
        
        def traverse(val:int, r:int, c:int) -> int:
            if r == R or c == C:
                return MAX
            
            v = val ^ grid[r][c]
            
            if r == R-1 and c == C-1:
                return v

            return min(
                traverse(v, r+1, c),
                traverse(v, r, c+1)
            )

        return traverse(0, 0, 0)

    def minCost_dp(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = [ [ set() for _ in range(C) ] for __ in range(R)]
        
        # row 0, col 0
        res[0][0].add(grid[0][0])
        # row 0 
        for c in range(1, C):
            for elem in res[0][c-1]:
                res[0][c].add( grid[0][c] ^ elem )
        
        for r in range(1, R):
            # col 0 
            for elem in res[r-1][0]:
                res[r][0].add( grid[r][0] ^ elem )
        
            # col 1->C-1
            for c in range(1, C):
                for elem in res[r][c-1]:
                    res[r][c].add( grid[r][c] ^ elem )
                for elem in res[r-1][c]:
                    res[r][c].add( grid[r][c] ^ elem )

        # for row in res:
        #     print(row)
        return min(res[-1][-1])

    def minCost_dp2(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = [ [None]*C for _ in range(R)]
        
        # row 0, col 0
        res[0][0] = set([grid[0][0]])
        # row 0 
        for c in range(1, C):
            res[0][c] = set( grid[0][c] ^ elem for elem in res[0][c-1] )
            
        for r in range(1, R):
            # col 0 
            res[r][0] = set( grid[r][0] ^ elem for elem in res[r-1][0] )
            
            # col 1->C-1
            for c in range(1, C):
                res[r][c] = set(
                    [ grid[r][c] ^ elem for elem in res[r-1][c] ] +\
                    [ grid[r][c] ^ elem for elem in res[r][c-1] ]
                )
                
        # for row in res:
        #     print(row)
        return min(res[-1][-1])

'''
0111
0010
0101
0101
0000
 
'''


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.minCost,
        sol.minCost_dp,
        sol.minCost_dp2
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
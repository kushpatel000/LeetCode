# 3665. Twisted Mirror Path Count [Medium]
# https://leetcode.com/problems/twisted-mirror-path-count/ 

from typing import List
import test_suite as ts

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])

        dp = [ [0]*C for _ in range(R) ]

        dp[0][0] = 1

        def flow(r, c, d, amt):
            '''
            r,c target coordinates
            d - direction coming from (0 - down, 1 - right)
            '''
            if r == R or c == C: return

            if grid[r][c] == 0:
                dp[r][c] += amt
            elif d == 0:
                flow(r, c+1, 1-d, amt)
            else:
                flow(r+1, c, 1-d, amt)


        for r in range(R):
            for c in range(C):
                # flow down
                flow(r+1, c, 0, dp[r][c])
                # flow right
                flow(r, c+1, 1, dp[r][c])
        
        # for row in grid:
        #     print(row)
        # print()
        # for row in dp:
        #     print(row)

        return dp[R-1][C-1] % (10**9+7)

    def uniquePaths_pc(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # precompute flows (in reverse direction)
        right_flow = [ [None]*C for _ in range(R) ]
        down_flow  = [ [None]*C for _ in range(R) ]
        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if grid[r][c] == 1:
                    right_flow[r][c] = down_flow[r+1][c] if r!=R-1 else None
                    down_flow[r][c] = right_flow[r][c+1] if c!=C-1 else None
                else:
                    right_flow[r][c] = (r,c)
                    down_flow[r][c] = (r,c)

                down_flow[0][c] = None
            right_flow[r][0] = None

        dp = [ [0]*C for _ in range(R) ]
        dp[0][0] = 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    # check right
                    xy = right_flow[r][c+1] if c < C-1 else None
                    if xy:
                        dp[xy[0]][xy[1]] += dp[r][c]
                    # check down
                    xy = down_flow[r+1][c] if r < R-1 else None
                    if xy:
                        dp[xy[0]][xy[1]] += dp[r][c]

        return dp[R-1][C-1] % (10**9+7)

        # for row in grid:    
        #     print(row)
        # print()
        # for row in right_flow:
        #     print(row)
        # print()
        # for row in down_flow:
        #     print(row)
        # print()

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.uniquePaths,
        sol.uniquePaths_pc
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
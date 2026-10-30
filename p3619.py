# 3619. Count Islands With Total Value Divisible by K [Medium]
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/ 

from typing import List
import test_suite as ts

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        def island_sum(r,c):
            if r<0 or r>=R or c<0 or c>=C or grid[r][c]==0:
                return 0

            a = grid[r][c]
            grid[r][c] = 0
            return a + \
                island_sum(r-1,c) + \
                island_sum(r+1,c) + \
                island_sum(r,c-1) + \
                island_sum(r,c+1)

        counts = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0 and island_sum(r,c) %k == 0:
                    counts += 1

        return counts

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.countIslands
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
# 3963. Create Grid With Exactly One Path [Easy]
# https://leetcode.com/problems/create-grid-with-exactly-one-path/ 

from typing import List
import test_suite as ts

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = ['#'*(n-1) + '.' for _ in range(m)]
        grid[0] = '.'*n
        return grid



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.createGrid
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
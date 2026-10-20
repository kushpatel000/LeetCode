# 1569. Number of Ways to Reorder Array to Get Same BST [Hard]
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/ 

from typing import List
import test_suite as ts
import math

M = 10**9 + 7

class Solution(object):
    def numOfWays(self, nums):
        def dfs(arr) -> int:
            if len(arr) < 3:
                return 1
            
            L, R = list(), list()
            for v in arr[1:]:
                if v > arr[0]:
                    R.append(v)
                else:
                    L.append(v)

            P = math.comb(len(arr)-1, len(L))
            return ( P*dfs(L)*dfs(R) ) % M

        return (dfs(nums)-1+M) % M

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.numOfWays
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
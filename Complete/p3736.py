# 3736. Minimum Moves to Equal Array Elements III [Easy]
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/ 

from typing import List
import test_suite as ts

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        M = max(nums)
        moves = sum(M - n for n in nums)

        return max(nums)*len(nums) - sum(nums)

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minMoves
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
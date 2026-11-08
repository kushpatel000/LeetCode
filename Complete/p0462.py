# 0462. Minimum Moves to Equal Array Elements II [Medium]
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/ 

from typing import List
import math
import test_suite as ts

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        mean = sum(nums) / len(nums)
        print(f'mean = {mean}')
        mean = int(mean) + ( (mean % 1) > 0.5 )
        print(f'mean = {mean}')
        return sum(abs(x - mean) for x in nums)
    
    def minMoves2_median(self, nums: list[int]) -> int:

        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(x - median) for x in nums)
        
        


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minMoves2,
        sol.minMoves2_median
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
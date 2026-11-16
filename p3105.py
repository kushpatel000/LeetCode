# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray [Easy]
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray 

#  You are given an array of integers nums. Return the length of the longest
#  subarray of nums which is either strictly increasing or strictly decreasing.
#  Example 1:
#  Input: nums = [1,4,3,3,2]
#  Output: 2
#  Explanation:
#  The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and
#  [1,4].
#  The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2],
#  and [4,3].
#  Hence, we return 2.
#  Example 2:
#  Input: nums = [3,3,3,3]
#  Output: 1
#  Explanation:
#  The strictly increasing subarrays of nums are [3], [3], [3], and [3].
#  The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
#  Hence, we return 1.
#  Example 3:
#  Input: nums = [3,2,1]
#  Output: 3
#  Explanation:
#  The strictly increasing subarrays of nums are [3], [2], and [1].
#  The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and
#  [3,2,1].
#  Hence, we return 3.
#  Constraints:
#  1 <= nums.length <= 50
#  1 <= nums[i] <= 50

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        best_incr, best_decr = 1, 1
        incr, decr = 1, 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                incr += 1
                best_incr = max(best_incr, incr)
                decr = 1
            elif nums[i] > nums[i+1]:
                decr += 1
                best_decr = max(best_decr, decr)
                incr = 1
            else:
                decr = 1
                incr = 1

        return max(best_incr, best_decr)




if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.longestMonotonicSubarray
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
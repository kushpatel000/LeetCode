# 3411. Maximum Subarray With Equal Products [Easy]
# https://leetcode.com/problems/maximum-subarray-with-equal-products 

#  You are given an array of positive integers nums.
#  An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr),
#  where:
#  prod(arr) is the product of all elements of arr.
#  gcd(arr) is the GCD of all elements of arr.
#  lcm(arr) is the LCM of all elements of arr.
#  Return the length of the longest product equivalent subarray of nums.
#  Example 1:
#  Input: nums = [1,2,1,2,1,1,1]
#  Output: 5
#  Explanation: 
#  The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1,
#  1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.
#  Example 2:
#  Input: nums = [2,3,4,5,6]
#  Output: 3
#  Explanation: 
#  The longest product equivalent subarray is [3, 4, 5].
#  Example 3:
#  Input: nums = [1,2,3,1,4,5,1]
#  Output: 5
#  Constraints:
#  2 <= nums.length <= 100
#  1 <= nums[i] <= 10

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

from math import gcd, lcm


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        ans = 1
        for i in range(N):
            # big_mat[i][i] = 
            p_prev, g_prev, l_prev = (nums[i],)*3
            for j in range(i+1,N):
                p = p_prev * nums[j]
                g = gcd(g_prev, nums[j])
                l = lcm(l_prev, nums[j])

                ans = max( ans, (j-i+1)*(p==g*l) )
                p_prev, g_prev, l_prev = p,g,l

        return ans        

    def maxLength_opt(self, nums: List[int]) -> int:
        N = len(nums)
        
        ans = 1
        for i in range(N):
            p_prev, g_prev, l_prev = (nums[i],)*3
            for j in range(i+1,N):
                p = p_prev * nums[j]
                g = gcd(g_prev, nums[j])
                l = lcm(l_prev, nums[j])

                if p > g*l: break
                if p==g*l:
                    ans = max(ans, j-i+1)
                p_prev, g_prev, l_prev = p,g,l

        return ans        


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.maxLength,
        sol.maxLength_opt
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
# 3727. Maximum Alternating Sum of Squares [Medium]
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/ 

from typing import List
import test_suite as ts

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        actual value doesn't matter, only the absolute value does
        
        1. sort descending by abs value
        2. first half is squared added
        3. second half is squared subtracted
        4. if odd, then the median goes to the add side
        '''
        nums.sort(key = lambda x: abs(x), reverse=True)
        sqsum = lambda L: sum(x**2 for x in L)
        h = (len(nums)+1) //2
        # print(nums[:h])
        # print(nums[h:])

        return sqsum(nums[:h]) - sqsum(nums[h:])



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
# 2778. Sum of Squares of Special Elements  [Easy]
# https://leetcode.com/problems/sum-of-squares-of-special-elements/ 

from typing import List
import test_suite as ts

class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum( [ n**2 for i,n in enumerate(nums) if len(nums)%(i+1)==0 ] )



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.sumOfSquares
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
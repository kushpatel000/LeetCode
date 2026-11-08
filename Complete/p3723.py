# 3723. Maximize Sum of Squares of Digits [Medium]
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/ 

from typing import List
import test_suite as ts

class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        n9, r = divmod(sum, 9)
        if n9 > num or (n9==num and r > 0): return ''

        res = '9'*n9
        if r > 0:
            res += str(r)
        res += '0'*(num-len(res))
        return res



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
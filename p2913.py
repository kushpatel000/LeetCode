# 2913. Subarrays Distinct Element Sum of Squares I [Easy]
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/ 

from typing import List
import test_suite as ts

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i+1,N+1):
                # print(nums[i:j])
                n = len(set(nums[i:j]))
                res += n**2
        return res

    def sumCounts_v2(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            elems = set()
            for j in range(i,N):
                elems.add(nums[j])
                res += len(elems)**2

        return res
        



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.sumCounts,
        sol.sumCounts_v2
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
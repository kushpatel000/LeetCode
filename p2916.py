# 2916. Subarrays Distinct Element Sum of Squares II [Hard]
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/ 

from typing import List
import test_suite as ts

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        M = 10**9 + 7
        N = len(nums)
        res = 0
        for i in range(N):
            elems = set()
            for j in range(i,N):
                elems.add(nums[j])
                res = (res + len(elems)**2) % M

        return res               

    def track_prev(self, nums: List[int]) -> int:
        M = 10**9 + 7
        N = len(nums)

        arr = [0] * N
        super_seen = set()
        for i in range(N):
            # 

        
        return res

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.sumCounts   ,
        sol.track_prev
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

'''



'''
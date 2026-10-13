# 2897. Apply Operations on Array to Maximize Sum of Squares [Hard]
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/ 

from typing import List
import test_suite as ts
import tqdm

class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        M = 10**9 + 7

        res = 0
        for i in tqdm.trange(k):
            for j in range(i+1,N):
                a,b = nums[i], nums[j]
                nums[i] = a | b
                nums[j] = a & b

            res = (res + nums[i] ** 2) % M
            # print( nums )

        # print(nums)
        return res

    def maxSum_v2(self, nums, k):
        N = len(nums)
        M = 10**9 + 7
        B = 31

        bits = [0] * B
        for v in nums:
            for p in range(B):
                if v & (2**p):
        
                    bits[p] += 1

        svals = [0] * k
        for p,nb in enumerate(bits):
            for i in range(min(nb,k)):
                svals[i] += 2**p

        return sum([ s**2 for s in svals ]) % M

    
    def maxSum_v3(self, nums, k):
        N = len(nums)
        M = 10**9 + 7
        B = 31

        bits = [0] * B
        for v in nums:
            i = 0
            while v:
                # print(v)
                if v & 1:
                    bits[i] += 1
                v = v >> 1
                i += 1
                
        svals = [0] * k
        for p,nb in enumerate(bits):
            for i in range(min(nb,k)):
                svals[i] |= (1<<p)

        return sum([ s**2 for s in svals ]) % M

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.maxSum,
        sol.maxSum_v2,
        sol.maxSum_v3
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # test = 1e9
    # for p in range(31):
    #     v = 2**p
    #     print(f'{v:14,d} - {v>test}')
# 3551. Minimum Swaps to Sort by Digit Sum [Medium]
# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/ 

from typing import List
import test_suite as ts

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0

        ds = [[sum(map(int, str(n))),n] for n in nums]
        
        argsort = sorted( list(range(N)), key=lambda i:ds[i] )

        seen = set()
        swaps = N
        for start in range(N):
            if start in seen:
                continue

            curr = start
            while curr not in seen:
                seen.add(curr)
                curr = argsort[curr]

            swaps -= 1
            
        return swaps


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minSwaps
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
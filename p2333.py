# 2333. Minimum Sum of Squared Difference [Medium]
# https://leetcode.com/problems/minimum-sum-of-squared-difference/ 

'''
Provided two arrays of integers. Compute the sum of square differences:
  SUM( (nums1-nums2)**2 )

Provided also 2 integers, k1 and k2. You can increment or decrement any 
element in nums1 by k1 number of times. Similarly with k2 and nums2. Array
elements will be >=0 but can be adjusted to be negative.

Find the minimum sum of square differences after making the allowed 
adjustments.



We basically just want to minimize the absolute difference between paired
elements. k1 and k2 independently do not really matter, the total adjustments
can be combined.

Since we are squaring the differences, we need to reduce the largest 
differences up to (k1+k2) times.

1. Make an array of the absolute difference.
2. Shave the top differences by up to (k1+k2) steps.

'''


from typing import List
import test_suite as ts

class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        n = len(nums1)
        steps = k1 + k2
        diff = sorted(
            [abs(a-b) for a,b in zip(nums1, nums2)], 
            reverse=True
        )

        if steps >= sum(diff): return 0

        import tqdm
        for i in range(n-1):
            delta = min( steps//(i+1), diff[i] - diff[i+1] )
            if delta == 0: continue

            for j in range(i, -1, -1):
                change = min(delta, steps)
                diff[j] -= change
                steps -= change
            # print(diff)
        
        # at this point, they're all the same value
        # if steps:
        d,r = divmod(steps, n)
        # print(f'{d=}, {r=}')
        for i in range(n):
            diff[i] -= d + (i<r)
            steps -= d + (i<r)

        # print(f'{diff}')
        # print(f'remaining steps: {steps}')
        return sum([a**2 for a in diff])

            
    def minSumSquareDiff_v2(self, nums1, nums2, k1, k2):
        N = 100_001
        steps = k1 + k2
        # print(f'{steps=}')
        
        diffs = [0] * N
        diffs[0] = 0
        diff_max = 0
        for a,b in zip(nums1, nums2):
            d = abs(a-b)
            diffs[d] += 1
            diff_max = max(diff_max, d)

        # print('PRE')
        # for d,c in enumerate(diffs):
        #     if c:
        #         print(f'd={d:6d} - {diffs[d]}')

    
        for i in range(diff_max, 0, -1):
            if diffs[i] == 0: continue

            shift = min(steps, diffs[i])
            diffs[i] -= shift
            diffs[i-1] += shift
            steps -= shift

            if steps == 0: break

        # print('POST')

        # for d,c in enumerate(diffs):
        #     if c:
        #         print(f'd={d:6d} - {diffs[d]}')

        return sum([ d**2 * diffs[d] for d in range(diff_max) ])

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.minSumSquareDiff,
        sol.minSumSquareDiff_v2,
        # sol.minSumSquareDiff_heap
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[4:],
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
# 3934. Smallest Unique Subarray [Hard]
# https://leetcode.com/problems/smallest-unique-subarray 

#  You are given an integer array nums.
#  Find the minimum length of a subarray that is not identical to any other
#  subarray in nums.
#  Return an integer denoting the minimum possible length of such a subarray.
#  Two subarrays are considered identical if they have the same length and the same
#  elements in corresponding positions.
#  Example 1:
#  Input: nums = [3,3,3]
#  Output: 3
#  Explanation:
#  Subarrays of length 1: [3] → appears 3 times
#  Subarrays of length 2: [3, 3] → appears 2 times
#  Subarrays of length 3: [3, 3, 3] → appears once
#  The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.
#  Example 2:
#  Input: nums = [2,1,2,3,3]
#  Output: 1
#  Explanation:
#  Subarrays of length 1:
#  [2] → appears 2 times
#  [1] → appears once
#  [3] → appears 2 times
#  The subarray [1] is unique, so the smallest unique subarray length is 1.
#  Example 3:
#  Input: nums = [1,1,2,2,1]
#  Output: 2
#  Explanation:
#  Subarrays of length 1:
#  [1] → appears 3 times
#  [2] → appears 2 times
#  Subarrays of length 2:
#  [1, 1] → appears once
#  [1, 2] → appears once
#  [2, 2] → appears once
#  [2, 1] → appears once
#  There is at least one subarray of length 2 that is unique, so the smallest
#  unique subarray length is 2.
#  Constraints:
#  1 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^5

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:

    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        candidates = set()
        seen = set()   

        N = len(nums)
        for s in range(N):
            for e in range(s,N):
                sub_arr = tuple(nums[s:e+1])
                if sub_arr in seen:
                    candidates.discard(sub_arr)
                else:
                    seen.add(sub_arr)
                    candidates.add(sub_arr)

        return min( map(len, candidates) )

    def smallestUniqueSubarray_opt(self, nums: List[int]) -> int:
        N = len(nums)
        # print(f'{N=}')
        for size in range(1,N):
            seen = set()
            candidates = set()

            for first in range(0,N+1-size):
                sub_arr = tuple(nums[first:first+size])
                if sub_arr in seen:
                    candidates.discard(sub_arr)
                else:
                    seen.add(sub_arr)
                    candidates.add(sub_arr)

            if candidates:
                return size

        return N


    def smallestUniqueSubarray_dict(self, nums: List[int]) -> int:
        N = len(nums)

        for size in range(1,N):
            counts = dict()
    
            for first in range(0,N+1-size):
                sub_arr = tuple(nums[first:first+size])
                counts[sub_arr] = counts.get(sub_arr, 0) + 1

            if 1 in counts.values():
                return size
                
        return N


    def smallestUniqueSubarray_dict_bin(self, nums: List[int]) -> int:
        N = len(nums)
        def has_unique(size:int) -> bool:
            counts = dict()
            for f in range(0,N+1-size):
                sub_arr = hash(tuple(nums[f:f+size]))
                counts[sub_arr] = counts.get(sub_arr, 0) + 1
                
            return 1 in counts.values()


        lo, hi = 0, N

        while hi - lo > 1:
            m = (hi+lo)//2
            # print(f'{lo=}, {m=}, {hi=}')
            if has_unique(m):
                hi = m
            else:
                lo = m
        # print(f'{hi=}')
        return hi
    

    import numpy as np
    def the_solution(self, nums: list[int]) -> int:
        n = len(nums)
        names = [np.unique(nums, return_inverse=True)[1]]  # names[k][i] is equal for equal windows nums[i:i + 2**k]
        for k in range(n.bit_length() - 1):  # blocks of 2, 4, 8, ... while they fit
            if 1 in np.bincount(names[k]):  # some block is unique already: longer ones are not needed
                break
            pairs = names[k][:-2 ** k] * n + names[k][2 ** k:]  # two halves as one number
            names.append(np.unique(pairs, return_inverse=True)[1])

        def found(length):  # is some window of this length unique?
            k = length.bit_length() - 1  # its first 2**k elements and its last 2**k cover it
            pairs = names[k][:n - length + 1] * n + names[k][length - 2 ** k:]
            return 1 in np.unique(pairs, return_counts=True)[1]

        return bisect_left(range(1, min(2 ** len(names), n)), True, key=found) + 1
            

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.smallestUniqueSubarray,
        sol.smallestUniqueSubarray_opt,
        sol.smallestUniqueSubarray_dict,
        sol.smallestUniqueSubarray_dict_bin
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True,
        # number=1,
        # repeat=1
    )
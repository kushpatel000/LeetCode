# 3942. Minimum Operations to Sort a Permutation [Medium]
# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/ 

from typing import List
import test_suite as ts

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        '''
        Operations are either reverse or rotate left; elements never change 
        neighbors. If the difference between two neighbors is not 1 or N, then
        it is not possible.
        
        The minimum should always be next to the maximum, except when it's at 
        the edge.
        >> [..., 0, N-1]
        >> [..., N-1, 0]
        >> [N-1, 0, ...]
        >> [0, N-1, ...]
        >> [..., 0, N-1, ...]
        >> [..., N-1, 0, ...]
        
        Basically, it's only possible if the array is alreay (sort of) sorted.
        '''
    
        N = len(nums)
    
        # solve the base cases (N = 1, 2)
        if N == 1: return 0
        if N == 2: return int(nums[0] > nums[1])

        # get the direction of the array
        if nums[1] - nums[0] == 1 or nums[1] - nums[0] == 1-N:
            d = 1
        else:
            d = -1
        # print(f'direction: {d}')
    
        # test possible
        # print(f'Checking for {d} or {-d*(N-1)}')
        for i in range(N-1):
            # print(f'{nums[i+1]} - {nums[i]} = {nums[i+1] - nums[i]}')
            # if nums[i+1] - nums[i] not in (d, -d*(N-1)):
            
            if nums[i+1]-nums[i] != d and nums[i+1]-nums[i] !=-d*(N-1):
                return -1

        # depending on direction, we need to rotate 0 in to either the first or
        # last position. Let I be the starting postiion of 0
        # 
        # If the direction is positive
        #   >> rotate 0 to the first position
        #       ==> Ops = I
        #   >> reverse (I' = N-I-1), rotate 0 to the last position (I'+1), reverse
        #       ==> Ops = 1 + (I'+1) + 1 = I' + 3 = N-I+2
        # if the direction is negative
        #   >> rotate 0 to the last position (I+1), then reverse
        #       ==> Ops = I+2
        #   >> reverse (I' = N-I-1), rotate 0 to the first position (I')
        #       ==> Ops = 1 + I' = 1 + N-I-1 = N-I
        I = nums.index(0)
        if d == 1:
            return min( I, N-I+2 )
        return min(I+2, N-I)


    def minOperations_opt(self, nums: List[int]) -> int:
        N = len(nums)
    
        def valid(v):
            inv = False
            for i in range(1,N):
                if v[i] < v[i-1]:
                    if inv: return False
                    inv = True
            return (not inv) or v[0]>v[N-1]

        ans = 10**9
        if valid(nums):
            i = nums.index(0)
            ans = min(i, N-i+2)
        
        rev = nums[::-1]
        if valid(rev):
            i = rev.index(0)
            ans = min(ans, 1+min(i,N-i))
        
        return ans if (ans < 10**9) else -1

    def minOperations_opt2(self, nums: List[int]) -> int:
            N = len(nums)
        
            def valid(v):
                inv = False
                for i in range(1,N):
                    if v[i] < v[i-1]:
                        if inv: return False
                        inv = True
                return (not inv) or v[0]>v[N-1]

            i = nums.index(0)
            if valid(nums):
                return min(i, N-i+2)
            
            if valid(nums[::-1]):
                return min(i+2, N-i)
            
            return -1

    def array_compare(self, nums: List[int]) -> int:
        N = len(nums)
        res = float('inf')
        target = list(range(N))

        k = nums.index(0)
        if nums[k:] + nums[:k] == target:
            res = min(res, k, N-k+2)

        rev_nums = nums[::-1]
        k_rev = rev_nums.index(0)
        if rev_nums[k_rev:] + rev_nums[:k_rev] == target:
            res = min(res, k_rev+1, N - k_rev + 1)

        if res == float('inf'):
            return -1
        return int(res)
    
    def array_compare_opt(self, nums: List[int]) -> int:
        N = len(nums)
        target = list(range(N))

        k = nums.index(0)

        # check forward
        if nums[k:] + nums[:k] == target:
            return min(k, N-k+2)

        # check reverse
        g = (k+1)%N
        # if N < 10:
        #     print('nums:',nums)
        #     print('recn:',nums[k:] + nums[:k])
        if nums[g:] + nums[:g] == target[::-1]:
            return min(N-k, k+2)
        
        return -1

    def winner(self, nums: List[int]) -> int:
        N = len(nums)
        k = nums.index(0)
        asc = desc = True

        for i in range(1,N):
            v = nums[(k+i)%N]
            if v != i: asc=False
            if v != (N-i): desc=False

            if not asc and not desc: return -1

        if asc:
            return min(k, N-k+2)
        return min(N-k, k+2)

    def winner_opt(self, nums: List[int]) -> int:
        N = len(nums)
        k = nums.index(0)
        asc = desc = True

        for i in range(1,N):
            v = nums[(k+i)%N]
            asc &= v != i
            desc &= v != (N-i)

            if not asc and not desc: return -1

        if asc:
            return min(k, N-k+2)
        return min(N-k, k+2)

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minOperations,
        sol.minOperations_opt,
        sol.minOperations_opt2,
        sol.array_compare,
        sol.array_compare_opt,
        sol.winner,
        sol.winner_opt
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

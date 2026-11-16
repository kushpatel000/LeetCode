# 1524. Number of Sub-arrays With Odd Sum [Medium]
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum 

#  Given an array of integers arr, return the number of subarrays with an odd sum.
#  Since the answer can be very large, return it modulo 10^9 + 7.
#  Example 1:
#  Input: arr = [1,3,5]
#  Output: 4
#  Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
#  All sub-arrays sum are [1,4,9,3,8,5].
#  Odd sums are [1,9,3,5] so the answer is 4.
#  Example 2:
#  Input: arr = [2,4,6]
#  Output: 0
#  Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
#  All sub-arrays sum are [2,6,12,4,10,6].
#  All sub-arrays have even sum and the answer is 0.
#  Example 3:
#  Input: arr = [1,2,3,4,5,6,7]
#  Output: 16
#  Constraints:
#  1 <= arr.length <= 10^5
#  1 <= arr[i] <= 100

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:
    def numOfSubarrays_brute(self, arr: list[int]) -> int:
        N = len(arr)
        ans = 0
        for i in range(N):
            for j in range(i,N):
               ans += sum(arr[i:j+1]) % 2
        return ans % (10**9+7)

    def numOfSubarrays(self, arr: list[int]) -> int:
        N = len(arr)
        arr = [ n % 2 for n in arr ]

        ans = 0
        for i in range(N):
            x = 0
            for j in range(i,N):
                x ^= arr[j]
                ans += x

        return ans % (10**9+7)

    def numOfSubarrays_cs(self, arr: list[int]) -> int:
        N = len(arr)
        arr[0] = arr[0] % 2
        for i in range(1,N):
            arr[i] = (arr[i-1] + arr[i]) % 2 
        
        ans = sum(arr)
        for i in range(N-1):
            for j in range(i+1,N):
                ans += (arr[j]-arr[i]) & 1

        return ans % (10**9+7)
    
    def numOfSubarrays_dp(self, arr: list[int]) -> int:
        # print(f'{arr=}')
        N = len(arr)
        dp = [[0,0], [0,0]]

        ans = 0 # counter

        for i in range(N):
            idx = i & 1
            P = arr[i] & 1

            # if this value's parity is even, adds to even sub-arrays
            # if this value's parity is odd, adds to odd sub-arrays
            dp[P][idx] = (1+dp[0][1-idx])
            dp[1-P][idx] = dp[1][1-idx]

            ans += dp[P][idx]
        
        return ans % (10**9+7)

    def numOfSubarrays_ps(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        count = prefix_sum = 0
        # even_count starts as 1 since the initial sum (0) is even
        odd_count = 0
        even_count = 1

        for num in arr:
            prefix_sum += num
            # If current prefix sum is even, add the number of odd subarrays
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            else:
                # If current prefix sum is odd, add the number of even
                # subarrays
                count += even_count
                odd_count += 1

            count %= MOD  # To handle large results

        return count



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.numOfSubarrays_brute,
        sol.numOfSubarrays,
        sol.numOfSubarrays_cs,
        sol.numOfSubarrays_dp,
        sol.numOfSubarrays_ps
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[:-1],
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )


    # for i in range(-5,6):
    #     print(f'{i:2d} % 2 = {i&1:2d}')
# 1477. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        sub_arrs = list()

        curr_sum = 0
        i = j = 0

        while i < len(arr):
            if curr_sum <= target:
                if j == len(arr): # can't add any more to increase sum
                    break
                else:
                    curr_sum += arr[j]
                    j += 1
            else:
                curr_sum -= arr[i]
                i += 1
            
            if curr_sum == target:
                sub_arrs.append((i,j))

        print(sub_arrs)
        if len(sub_arrs) < 2: return -1

        best_length = 2*len(arr)
        for i in range(len(sub_arrs)-1):
            ix, iy = sub_arrs[i]
            li = iy - ix
            for j in range(i+1, len(sub_arrs)):
                jx, jy = sub_arrs[j]
                lj = jy - jx 

                if li+lj < best_length and iy <= jx:
                    best_length = li+lj

        if best_length > len(arr): return -1
        return best_length

    def minSumOfLengths_v2(self, arr: list[int], target: int) -> int:

        best_length = 2*len(arr)
        best_A_before_i = 2*len(arr)

        overlapped_sub_arrs = list()

        curr_sum = 0
        i = j = 0
        while i < len(arr):
            if curr_sum <= target:
                if j == len(arr): # can't add any more to increase sum
                    break
                else:
                    curr_sum += arr[j]
                    j += 1
            else:
                curr_sum -= arr[i]
                i += 1
                while overlapped_sub_arrs and i >= overlapped_sub_arrs[0][1]:
                    m,n = overlapped_sub_arrs.pop(0)
                    best_A_before_i = min( best_A_before_i, n-m )
            
            if curr_sum == target:
                if j-i < best_A_before_i:
                    overlapped_sub_arrs.append((i,j))
                best_length = min(best_length, best_A_before_i + j-i)


        if best_length > len(arr): return -1
        return best_length

    def minSumOfLengths_v3(self, arr: list[int], target: int) -> int:
        '''simplified iterator'''
        AL = len(arr)
        best_length = 2*AL
        best = [2*AL] * AL

        curr_sum = 0
        i = 0
        for j in range(AL):
            curr_sum += arr[j]
            while curr_sum > target:
                curr_sum -= arr[i]
                i += 1

            best[j] = best[j-1]
            if curr_sum == target:
                best[j] = min( best[j-1], j-i+1 )
                
                if i > 0:
                    test = j-i+1 + best[i-1]
                    best_length = min(best_length, test)

        if best_length > len(arr): return -1
        return best_length


if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        # sol.minSumOfLengths,
        sol.minSumOfLengths_v2,
        sol.minSumOfLengths_v3,
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[:-1],
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


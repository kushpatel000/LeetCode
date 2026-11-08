# 1385. Find the Distance Value Between Two Arrays [Easy]
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/ 

from typing import List
import test_suite as ts

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        all_out = lambda x: all([abs(x-j)>d for j in arr2])
        return sum( all_out(a) for a in arr1 )
        
    def findTheDistanceValue_bisect(self, arr1: list[int], arr2: list[int], d: int) -> int:
        import bisect
        arr2.sort()

        print(arr2)
        counts = 0
        for k in arr1:
            idx = bisect.bisect_left(arr2, k)
            print(f'{k=}, {idx=}')
            if idx == 1 and abs(arr2[0] - k) <= d:
                continue
            if idx < len(arr2) and abs(arr2[idx] - k) <= d:
                continue
            if idx < len(arr2)-1 and abs(arr2[idx+1] - k) <= d:
                continue
            counts += 1
        return counts


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.findTheDistanceValue,
        sol.findTheDistanceValue_bisect
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 
        # 1e-5,

        display = True,
        test_only = True
    )
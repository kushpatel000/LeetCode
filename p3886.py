# 3886. Sum of Sortable Integers [Hard]
# https://leetcode.com/problems/sum-of-sortable-integers/ 

from typing import List
import test_suite as ts

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        def check_sortable(a:list[int]):
            b = sorted(a)
            return ','.join(map(str,b)) in ','.join(map(str,a+a))


        N = len(nums)
        res = 0
        if check_sortable(nums): res += N
        print(f'{res=}')

        for k in range(1,N//2+1):
            print(f'{k=}')
            if not N%k==0: continue
            
            last_max = 0 
            valid = True
            for i in range(0,N,k):
                arr = nums[i:i+k]   
                print(f'{i=} {arr=}')
                valid &= min(arr) >= last_max
                valid &= check_sortable(arr)
                if not valid: break
                last_max = max(arr)


            res += valid*k

        return res

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.sortableIntegers
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
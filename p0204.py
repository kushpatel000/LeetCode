# 0204. Count Primes

# from functools import cache
from typing import List
import test_suite as ts


class Solution:
    def countPrimes(self, n:int)-> int: 
        if n < 3: return 0

        arr = [True]*(n)
        arr[0] = False
        arr[1] = False
        for k in range(2,n):
            for i in range(2*k,n,k):
                arr[i] = False
        
        return sum(arr)

    def countPrimes_v2(self, n:int)-> int: 
        if n < 3: return 0

        arr = [True]*(n)
        arr[0] = False
        arr[1] = False

        for k in range(2,n):
            if arr[k]:
                for i in range(2*k,n,k):
                    arr[i] = False
        
        return sum(arr)

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_cases = ts.load_test_cases(__file__)

    test_funcs = [
        sol.countPrimes,
        sol.countPrimes_v2,
    ]

    ts.test_all(
        test_cases,
        test_funcs,
        check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )


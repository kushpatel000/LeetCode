# 0204. Count Primes

# from functools import cache
from typing import List
import test_suite as ts


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        primes = list()

        arr = [True]*(right+1)
        arr[0] = arr[1] = False
        for k in range(2, right+1):
            if arr[k]:
                if k >= left: primes.append(k)
                for j in range(2*k, right+1, k):
                    arr[j] = False

        # print(primes)
        
        if len(primes) < 2:
            return [-1,-1]
        
        num1, num2 = primes[0], primes[-1]
        for i in range(len(primes)-1):
            d = primes[i+1] - primes[i]
            if d < num2-num1:
                num1, num2 = primes[i], primes[i+1]
        
        return [num1,num2]

    def closestPrimes_v2(self, left: int, right: int) -> list[int]:
        p1,p2 = 0,0

        arr = [True]*(right+1)
        arr[0] = arr[1] = False
        for k in range(2, right+1):
            if arr[k]:
                if k >= left: 
                    if k-p2 < p2-p1 or p2 == 0:
                        p1, p2 = p2, k
                    
                for j in range(2*k, right+1, k):
                    arr[j] = False

        if p1 == 0:
            return [-1, -1]
        return [p1, p2]


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_cases = ts.load_test_cases(__file__)

    test_funcs = [
        sol.closestPrimes,
        sol.closestPrimes_v2,
    ]

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )


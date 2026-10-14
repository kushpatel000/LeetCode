# 4022. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def kthDigit_brute(self, k:int) -> int:
        string = ''
        for b in range(30):
            s, f = 10*b, 10*b+9
            if b%2 == 1:
                for n in range(f, s-1, -1):
                    string += str(n)
            else:
                for n in range(s, f+1):
                    string += str(n)

            if len(string) > k:
                break

        return int(string[k])

    def kthDigit(self, k:int) -> int:
        block0 = 9 # == 9*1
        block9 = 180 # == 90 * 2 
        block99 = 2700 # == 900 * 3
        block999 = 36_000 # == 9000 * 4

        ndigs = 0
        magnitude = 0
        for m in range(15):
            new_digs = 9 * 10**m * (m+1)
            if k < ndigs + new_digs:
                magnitude = m
                break
        
            ndigs += new_digs

        k -= ndigs
        block = k // (10 * (m+1))

        print(magnitude, ndigs, block)


if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.kthDigit_brute
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

    # a = []
    # b = []

    # for m in range(5):
    #     a.append( 9 * 10**m * (m+1) )

    #     res = ''
    #     for k in range(10**m, 10**(m+1)):
    #         res += str(k)
    #     b.append(len(res))

    # for aa,bb in zip(a,b):
    #     print(f'{aa} {bb} {aa==bb}')
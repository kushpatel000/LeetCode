# 0233. Number of Digit One

# from functools import cache
from typing import List
import test_suite as ts

test_cases = [
    [
        13,
        6
    ],
    [
        11,
        4
    ]
]

class Solution:
    def countDigitOne(self, n:int)-> int: 
        N = n
        counts = 0
        for o in range(9,0,-1):
            d, N = divmod( N, int(10**o) )
            if d==0: continue

            per_dec = o*10**(o-1)
            # print(f'{o=}, {per_dec=}, {d=}, {N=}')

            if d == 1:
                counts += (N+1)
            if d > 0: # everything under this
                counts += d*per_dec
            if d > 1: # add the extra ones covered
                counts += 10**o 

        # print(f'{results[n]=} {counts=}')
        if N > 0: counts += 1
        return int(counts)
        # print(counts)

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.countDigitOne,
    ]

    # ts.test_all(
    #     test_cases,
    #     test_funcs,
    #     check_thresh = 1e-5,
    #     display = True,
    #     test_only = True
    # )



    curr = 0
    for k in range(100000):
        curr += str(k).count('1')
        res = sol.countDigitOne(k)

        if curr != res:
            print(f'{k:2d}, {curr:2d}, {res:2d}, {res-curr:2d}')
    

    
    # ts.check_soln(
    #     sol.countDigitOne,
    #     11,
    #     4,
    #     lambda a,b: a==b,
    #     display=True
    # )
    
    

# 1866. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts
import itertools
import math


M = 10**9 + 7
class Solution:
    @cache
    def _fact(self, n:int) -> int:
        if n == 0: return 1
        return n * self._fact(n-1) % M

    def brute_force(self, n:int, k:int, show=False):
        nums = list(range(1,n+1))

        res = 0
        for perm in itertools.permutations(nums):
            curr_max = 0
            visible = 0
            for p in perm:
                if p > curr_max:
                    visible += 1
                    curr_max = p

            if visible == k:
                res += 1
                if show: print(perm)

        return res

    @cache
    def rearrangeSticks(self, n: int, k: int) -> int:
        if n == k: return 1
    
        # = Sum[i=0->n-1] nCr(n-1,i) * rearrangeSticks(i,k-1) * (n-i-1)!
        opts = 0 
        for i in range(n):
            left_combs = math.comb(n-1, i)                  % M
            left_valid = self.rearrangeSticks(i, k-1)       % M
            right_combs = self._fact(n-i-1)                 % M
            opts += left_combs * left_valid * right_combs

        return opts % M

    @cache
    def RS_opt(self, n: int, k: int) -> int:
        if 0 in (n,k): return 0
        if n == k: return 1
        if k == 1: return self._fact(n-1)
        return ((n-1) * self.RS_opt(n-1,k) + self.RS_opt(n-1,k-1))%M




if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.rearrangeSticks,
        sol.RS_opt
    ]
    
    test_cases = ts.load_test_cases(__file__)

    # ts.test_all(
    #     test_cases,
    #     test_funcs,
    #     # check_thresh = 1e-5,
    #     display = True,
    #     test_only = True
    # )




    n = 5

    for k in range(n+1):
        p = sol.RS_opt(n,k)
        print(f'C({n},{k}) = {math.comb(n,k):2,d} P({n},{k}) = {p:3,d}')
    print()

    n = 7

    for k in range(n+1):
        p = sol.RS_opt(n,k)
        print(f'C({n},{k}) = {math.comb(n,k):2,d} P({n},{k}) = {p:3,d}')

    RES = 
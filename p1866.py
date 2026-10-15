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


    @cache
    def RS_opt_2(self, n: int, k: int) -> int:
        if 0 in (n,k): return 0
        if n == k: return 1
        if k == 1: return self._fact(n-1)

        R = range(2,n)
        res = 0
        for e in itertools.combinations(R, n-k):
            res += math.prod(e) % M
        for e in itertools.combinations(R, n-k-1):
            res += math.prod(e) % M

        return res % M


    def RS_opt_3(self, n: int, k: int) -> int:
        # self._dc = dict()

        facts = [1]*(n+1)
        for i in range(1,n+1):
            facts[i] = (facts[i-1]*i) %M

        @cache
        def soln(n_,k_):
            # self._dc[(n_,k_)] = self._dc.get((n_,k_), 0) + 1
            # if 0 in (n_,k_): return 0
            if n_ == k_: return 1
            if k_ == 1: return facts[n_-1]

            return ( (n_-1)*soln(n_-1,k_) + soln(n_-1,k_-1) ) % M

        
        return soln(n,k) 
                        



if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        # sol.rearrangeSticks,
        sol.RS_opt,
        # sol.RS_opt_2,
        sol.RS_opt_3,
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # print(sol._dc)
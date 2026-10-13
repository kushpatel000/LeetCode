# 4073. Count Good Strings

from functools import cache
from math import sqrt
from typing import List
import test_suite as ts

class Solution:
    # One of the possible inputs is 1e15, so there must be a mathematical
    # formula to describe this.
    # Turns out, its just twice the Fibonacci sequence

    @cache
    def countGoodStrings_recurse(self, n:int) -> int:
        if n == 1 or n == 2: return 2
        return (self.countGoodStrings_recurse(n-1) + self.countGoodStrings_recurse(n-2)) % 1000000007

    @cache
    def countGoodStrings_iterate(self, n:int) -> int:
        a,b = 2,2
        for k in range(3,n+1):
            a,b = b, (a+b)%1000000007
        return b

    def countGoodStrings_calc(self, n:int) -> int:
        phi = (1+sqrt(5)) / 2
        psi = (1-sqrt(5)) / 2

        a = (phi**n - psi ** n) / sqrt(5)
        return int(2*a) % 1000000007
    
    def countGoodStrings_df(self, n:int) -> int:
        # using fast doubling

        @cache
        def fib(n):
            if n < 3: return 1

            k = n//2
            if n % 2 == 0:
                r = fib(k) * ( 2*fib(k+1) - fib(k) )
            else:
                r = fib(k)**2 + fib(k+1)**2
            
            return r % 1000000007

        return (2*fib(n)) % 1000000007

    
@cache
def is_good_string(s:str) -> bool:
    n = len(s)
    if n == 0: return False

    if n%2==1 and s == s[0]*n:
        return True

    for i in range(1,n):
        l = s[:i]
        r = s[i:]
        if l[-1] != r[0] and is_good_string(l) and is_good_string(r):
            return True

    return False

@cache
def fibonacci(n:int) -> int:
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)

@cache
def fibonacci_fd(n:int) -> int:
    if n < 3: return 1

    k = n//2
    if n % 2 == 0:
        return fibonacci_fd(k) * ( 2*fibonacci_fd(k+1) - fibonacci_fd(k) )
    else:
        return fibonacci_fd(k)**2 + fibonacci_fd(k+1)**2
    

def generate_all_strings(n:int):
    for i in range(2**n):
        yield f'{i:0{n}b}'



if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        # sol.countGoodStrings_recurse,
        sol.countGoodStrings_iterate,
        # sol.countGoodStrings_calc,
        sol.countGoodStrings_df,
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


    # for k in range(1,15):
    #     a = fibonacci(k)
    #     b = fibonacci_fd(k)
    #     print(f'{k} {a==b}, {a}, {b}')
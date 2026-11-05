# 2217. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def kthPalindrome_naive(self, queries: list[int], intLength: int) -> list[int]:
        # print(queries, intLength)
        n = intLength // 2

        pc = 0
        qp = 0
        res = list()

        # if even handle one way
        if intLength % 2 == 0:
            for k in range(10**n):
                s = f'{k:0{n}d}'
                if s[0] == '0': continue

                p = s + s[::-1]
                pc += 1

                if pc == queries[qp]:
                    res.append(p)
                    qp += 1
                    if qp == len(queries): break

                
        # if odd, slightly differnetly
        else:
            for k in range(10**n):
                s = f'{k:0{n}d}'
                if s[0] == '0': continue

                for d in range(10):
                    p = s + str(d) + s[::-1]
                    pc += 1

                    if pc == queries[qp]:
                        res.append(p)
                        qp += 1
                        if qp == len(queries): break

                if qp == len(queries): break

        return list(map(int, res))

    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        num_palindromes = 9 * 10**( (intLength-1)//2 )

        mirror_digits = intLength//2
        base = 10**(mirror_digits-1)

        def make(n:int):
            if n > num_palindromes: return -1

            if intLength % 2 == 0:
                s = str(base + n - 1)
                return int( s + s[::-1] )
            else:
                d,r = divmod(n-1, 10)
                s = str(base + d)
                return int( s + str(r) + s[::-1] )

        if intLength == 1:
            return [ n if n < 10 else -1 for n in queries ]
        return [ make(n) for n in queries ]

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.kthPalindrome_naive,
        sol.kthPalindrome
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # import tqdm
    
    # by_digit = [0] * 7
    # for k in tqdm.trange( 1, 10**(len(by_digit)-1) ):
    #     s = str(k)
    #     if s == s[::-1]:
    #         by_digit[ len(s) ] += 1

    # for i, n in enumerate(by_digit):
    #     print(f'{i}: {n} {((i+1)//2)}')


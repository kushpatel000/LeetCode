# 0172. Trailing Zeros

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        The number of trailing zeros depends on how many 5's and 2's divide
        n!. Note there will always be less 5's than 2's. So we actually just
        need to count the number of 5's.
        '''
        counts = 0
        for k in range(5,n+1,5):
            # print(k)
            for e in range(1, 7):
                if k % (5**e) == 0:
                    counts += 1
                else:
                    break
            # print('  ', counts )
        return counts

    def trailingZeroes_log(self, n: int) -> int:
        counts = 0

        while n > 0:
            counts += n//5
            n = n//5

        return counts

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.trailingZeroes,
        sol.trailingZeroes_log
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # for e in range(10):
    #     p = 5**e
    #     print(f'5**{e} = {p:6,d}')
    #     if p > 10**4: break
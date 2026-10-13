# 0087. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)
        for i in range(1, n):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                return True
            if (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False

    def all_scrambles(self, s:str) -> set[str]:
        if len(s) <= 1:
            return {s}
        scrambles = set()
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            left_scrambles = self.all_scrambles(left)
            right_scrambles = self.all_scrambles(right)
            for l in left_scrambles:
                for r in right_scrambles:
                    scrambles.add(l + r)
                    scrambles.add(r + l)
        return scrambles

    def isScramble_yield(self, s1: str, s2: str) -> bool:
        def scramble_generator(s:str):
            if len(s) <= 1:
                yield s
            else:
                for i in range(1, len(s)):
                    left = s[:i]
                    right = s[i:]
                    for l in scramble_generator(left):
                        for r in scramble_generator(right):
                            yield l + r
                            yield r + l

        for g in scramble_generator(s1):
            if g == s2:
                return True
        # return s2 in scramble_generator(s1)

    @cache
    def factorial(self, n:int) -> int:
        if n <= 1:
            return 1
        return n * self.factorial(n-1)

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.isScramble,
        sol.isScramble_yield
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # word = 'abcdefg'
    # scrambles = sol.all_scrambles(word)
    # for r in scrambles:
    #     print(r , end ='')
    #     # if r.startswith('ca'):
    #     #     print(' <--', end='')
    #     print()


    # print(f"Factorial: {sol.factorial(len(word))}")
    # print(f"Actual: {len(scrambles)}")
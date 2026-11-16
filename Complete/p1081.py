# 1081. Smallest Subsequence of Distinct Characters

from functools import cache
from typing import List
import test_suite as ts
import collections

class Solution:
    def smallestSubsequence_old(self, s: str) -> str:
        ctr = collections.Counter(s)
        stack = []
        added = set()
        
        for c in s:
            if c not in added:
                while stack and c < stack[-1] and ctr[stack[-1]] > 0:
                    added.remove(stack.pop())
                stack.append(c)
                added.add(c)
            ctr[c] -= 1
        
        return ''.join(stack)

    # def smallestSubsequence(self, s: str) -> str:
    #     rel_ord = lambda c: ord(c)-ord('a')

    #     ctr = [0]*26
    #     for c in s:
    #         ctr[rel_ord(c)] += 1

    #     stack = []
    #     mask = 0
    #     print(s)
    #     for c in s:
    #         b = 1<<rel_ord(c)
    #         if not mask & b:
    #             while stack and c < stack[-1] and ctr[rel_ord(stack[-1])] > 0:
    #                 d = 1 << rel_ord(stack.pop())
    #                 mask ^= d
    #         stack.append(c)
    #         mask |= b

    #     return ''.join(stack)


if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.smallestSubsequence_old,
        # sol.smallestSubsequence
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


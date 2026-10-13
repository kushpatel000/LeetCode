# 1541. Minimum Insertions to Balance a Parentheses String [Medium]
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/ 

from typing import List
import test_suite as ts

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """

        # stack = []
        d = 0
        add = 0
        i = 0
        while i < len(s):
            c = s[i]
        
            # open, increase stack
            if c == '(':
                d += 1
                i += 1

            # close, but no stacks to close
            elif d == 0:
                add += 1
                # check if this close is single
                if i == len(s)-1 or s[i+1] != ')':
                    add += 1
                    i += 1
                else:
                    i += 2

            # close, but has stacks to close
            else:
                d -= 1
                # check if this close is single
                if i == len(s)-1 or s[i+1] != ')':
                    add += 1
                    i += 1
                else:
                    i += 2
                 
        return add + 2*d

    def minInsertions_v2(self, s):
        """
        :type s: str
        :rtype: int
        """

        # stack = []
        d = 0
        add = 0
        i = 0
        while i < len(s):
            # open, increase stack
            if s[i] == '(':
                d += 1

            # close
            else:
                # no stacks to close
                if d == 0:
                    add += 1
                else:
                    d -= 1

                # check if this close is single
                if i == len(s)-1 or s[i+1] != ')':
                    add += 1
                else:
                    i += 1

            i += 1
            
        return add + 2*d


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minInsertions,
        sol.minInsertions_v2
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
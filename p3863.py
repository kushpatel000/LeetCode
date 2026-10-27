# 3863. Minimum Operations to Sort a String [Medium]
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/ 

from typing import List
import test_suite as ts

class Solution:
    def minOperations(self, s: str) -> int:
        # check sorted
        print([ i<j for i,j in zip(s,s[1:]) ])
        if all([ i<j for i,j in zip(s,s[1:]) ]):
            return 0
        # then not sorted

        if len(s) == 2:
            return -1
        # then possible

        l,r = min(s), max(s)

        # if one of the extremes is in place, the sort all the remainders
        if s[0] == l or s[-1] == r:
            return 1

        # if an extreme exists in the middle, then 2
        if l in s[1:-1] or r in s[1:-1]:
            return 2

        # worst case
        return 3




if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minOperations
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

    print(sorted('dbca'))
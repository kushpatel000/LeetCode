# 2089. Find Target Indices After Sorting Array [Easy]
# https://leetcode.com/problems/find-target-indices-after-sorting-array/ 

from typing import List
import test_suite as ts

import bisect

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        count = nums.count(target)
        lower_than = sum([ n < target for n in nums ])
        print(f'{target=}, {count=}, {lower_than=}')
        return list(range(lower_than, lower_than+count))


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.targetIndices
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
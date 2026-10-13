# 3550. Smallest Index With Digit Sum Equal to Index


from functools import cache
from typing import List
import test_suite as ts

test_cases = [
    [
        [1,3,2], 
        2
    ],
    [
        [1,10,11],
        1
    ],
    [
        [1,2,3],
        -1
    ]
]

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ds = lambda n: sum([ int(c) for c in str(n) ])

        for i, n in enumerate(nums):
            if i == ds(n):
                return i
        
        return -1

    def smallestIndex_index(self, nums: List[int]) -> int:
        p = '0123456789'
        ds = lambda n: sum([ p.index(c) for c in str(n) ])
        
        for i, n in enumerate(nums):
            if i == ds(n):
                return i
        
        return -1
    
    def smallestIndex_find(self, nums: List[int]) -> int:
        p = '0123456789'
        ds = lambda n: sum([ p.find(c) for c in str(n) ])
        
        for i, n in enumerate(nums):
            if i == ds(n):
                return i
        
        return -1
        
    def smallestIndex_divmod(self, nums: List[int]) -> int:
        def ds(n:int) -> int:
            d = n
            s = 0
            while d > 0:
                d, r = divmod(d, 10)
                s += r
            return s
            
        for i, n in enumerate(nums):
            if i == ds(n):
                return i
        
        return -1
        

    
if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.smallestIndex,
        sol.smallestIndex_index,
        sol.smallestIndex_find,
        sol.smallestIndex_divmod,
    ]

    # test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,#[-1:],
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
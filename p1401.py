# 1401. Circle and Rectangle Overlapping

# from functools import cache
from typing import List
import test_suite as ts

test_cases = [
    [
        [1, 0, 0, 1, -1, 3, 1], 
        True
    ], 
    [
        [1, 1, 1, 1, -3, 2, -1], 
        False
    ], 
    [
        [1, 0, 0, -1, 0, 0, 1],
        True
    ]
]

class Solution:
    def checkOverlap(self, pack:list)-> bool: 
        radius, xCenter, yCenter, x1, y1, x2, y2 = pack
        
        def three_check(lo,hi,ct):
            if ct < lo: return lo
            if ct > hi: return hi
            return ct
    
        cx = three_check(x1,x2,xCenter)
        cy = three_check(y1,y2,yCenter)

        return radius**2 >= (cx-xCenter)**2 + (cy-yCenter)**2

    def checkOverlap_minmax(self, pack:list)-> bool:
        radius, xCenter, yCenter, x1, y1, x2, y2 = pack
                

        def three_check(lo,hi,ct):
            return min(max(lo, ct), hi)
        
        cx = three_check(x1,x2,xCenter)
        cy = three_check(y1,y2,yCenter)

        return radius**2 >= (cx-xCenter)**2 + (cy-yCenter)**2

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.checkOverlap,
        sol.checkOverlap_minmax,
    ]

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
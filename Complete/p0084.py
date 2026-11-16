# 0084. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # initialization covers the 1-by-h rectangles
        max_area = max(heights)

        stack = list()

        for i,h in enumerate(heights):
            print(f'{i=}, {h=}, {stack=}')
            while stack and heights[stack[-1]] > h:
                stack.pop()
            print(f'  {stack=}')

            if stack:
                areas = [ (i-j+1)*min(h,heights[j]) for j in stack ]
                print(f'  {areas=}')
                max_area = max( max_area, max(areas) )
            
            stack.append(i)

        return max_area




if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.largestRectangleArea
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


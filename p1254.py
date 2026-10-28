# 1254. Number of Closed Islands [Medium]
# https://leetcode.com/problems/number-of-closed-islands/ 

from typing import List
import test_suite as ts

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        R,C = len(grid), len(grid[0])

        def _traverse(r:int, c:int, to:int) -> bool:
            if r < 0 or r >= R or c < 0 or c >= C:
                return 0
            
            elif grid[r][c] == 1 or grid[r][c] == 2:
                return 1

            grid[r][c] = to
            u = _traverse(r-1,c,to) > 0
            d = _traverse(r+1,c,to) > 0
            l = _traverse(r,c-1,to) > 0
            r = _traverse(r,c+1,to) > 0

            if all([u,d,l,r]): return 2
            else: return 0


        # def print_matrix():
        #     for row in grid:
        #         print(' '.join([ str(x) for x in row ]))
        #     print()

        # print("original")
        # print_matrix()
        count = 0 
        # iterate over all internal cells and count the number of results
        # cells = list()
        for r in range(1,R-1):
            for c in range(1,C-1):
                if _traverse(r,c,2) == 2:
                    # cells.append((r,c))
                    count += 1

                    # print((r,c))
                    # print_matrix()
        # print(f'\nFinal Counts: {count}')

        return count

    def closedIsland_v2(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def _traverse(r:int, c:int) -> bool:
            if r < 0 or r >= R or c < 0 or c >= C:
                return

            if grid[r][c] == 0:
                grid[r][c] = 1
                _traverse(r-1,c)
                _traverse(r+1,c)
                _traverse(r,c-1)
                _traverse(r,c+1)

        # convert edges
        for c in range(C):
            _traverse(0,c)
            _traverse(R-1,c)
        
        for r in range(R):
            _traverse(r,0)
            _traverse(r,C-1)

        counts = 0
        for r in range(1,R-1):
            for c in range(1,C-1):
                if grid[r][c] == 0:
                    counts +=1
                    _traverse(r,c)

        return counts

        



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.closedIsland,
        sol.closedIsland_v2,
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
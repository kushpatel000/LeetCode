# 1267. Count Servers that Communicate [Medium]
# https://leetcode.com/problems/count-servers-that-communicate 

#  You are given a map of a server center, represented as a m * n integer
#  matrix grid, where 1 means that on that cell there is a server and 0 means that
#  it is no server. Two servers are said to communicate if they are on the same row
#  or on the same column.
#  Return the number of servers that communicate with any other server.
#  Example 1:
#  Input: grid = [[1,0],[0,1]]
#  Output: 0
#  Explanation: No servers can communicate with others.
#  Example 2:
#  Input: grid = [[1,0],[1,1]]
#  Output: 3
#  Explanation: All three servers can communicate with at least one other server.
#  Example 3:
#  Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
#  Output: 4
#  Explanation: The two servers in the first row can communicate with each other.
#  The two servers in the third column can communicate with each other. The server
#  at right bottom corner can't communicate with any other server.
#  Constraints:
#  m == grid.length
#  n == grid[i].length
#  1 <= m <= 250
#  1 <= n <= 250
#  grid[i][j] == 0 or 1

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        servers = set()
        # rows
        for r in range(M):
            if sum(grid[r]) > 1:
                for c in range(N):
                    if grid[r][c]: servers.add((r,c))

        # cols
        for c, col in enumerate(zip(*grid)):
            if sum(col) > 1:
                for r in range(M):
                    if grid[r][c]: servers.add((r,c))


        return len(servers)

    def countServers_setadd(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        servers = set()
        # rows
        for r in range(M):
            if sum(grid[r]) > 1:
                servers.update([ (r,c) for c in range(N) if grid[r][c] ])

        # cols
        for c, col in enumerate(zip(*grid)):
            if sum(col) > 1:
                servers.update([ (r,c) for r in range(M) if grid[r][c] ])


        return len(servers)

    def countServers_seen(self, grid: list[list[int]]) -> int:
        rows = set()
        cols = set()
        server_count = 0
        seeds = list()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    if r in rows or c in cols:
                        server_count += 1
                    else:
                        seeds.append((r,c))
                    rows.add(r)
                    cols.add(c)

        # for row in grid:
        #     print(row)
        # print(seeds)

        for sr, sc in seeds:
            if sum(grid[sr]) > 1 or sum([row[sc] for row in grid]) > 1:
                server_count += 1
        
        return server_count

    def countServers_fast(self, grid: list[list[int]]) -> int:
        c=0
        for i in grid:
            sm=sum(i)
            if sm==1:
                t=[l for l in range(len(i)) if i[l]==1] 
                cc=0
                for j in range(len(grid)):
                    if grid[j][t[0]]==1:
                        cc+=1
                if cc<2:
                    c-=1
            c+=sm
        return c

    def countServers_fast2(self, grid: list[list[int]]) -> int:
            c=0
            for i in grid:
                sm=sum(i)
                if sm==1:
                    t=[l for l in range(len(i)) if i[l]==1] 
                    cc = sum([row[t[0]] for row in grid])
                    if cc<2:
                        c-=1
                c+=sm
            return c

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.countServers,
        sol.countServers_setadd,
        sol.countServers_seen,
        sol.countServers_fast,
        sol.countServers_fast2
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True,
        number=10_000
    )
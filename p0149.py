# 0149. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        npts = len(points)
        lines = dict()

        for i in range(npts-1):
            pi = points[i]
            lines[i] = dict()

            for j in range(i+1, npts):
                pj = points[j]
                j_run  = pj[0] - pi[0]
                j_rise = pj[1] - pi[1]


                for r_run, r_rise in lines[i].keys():
                    if j_run * r_rise == j_rise * r_run:
                        lines[i][(r_run, r_rise)].append(j)
                        break

                # not found, so add:
                lines[i][(j_run,j_rise)] = [j]
        
        # for i in lines.keys():
        #     print(f'==== {i:2d} ====')
        #     for k,v in lines[i].items():
        #         print(f'{k}: {v}')
        #     print()


        if len(lines) == 0: return 1
        return 1+max([len(a) for b in lines.values() for a in b.values() ])

    def maxPoints_count(self, points: list[list[int]]) -> int:
        if len(points) <= 2: return len(points)

        npts = len(points)
        lines = dict()

        for i in range(npts-1):
            pi = points[i]
            for j in range(i+1, npts):
                pj = points[j]
                jdx = pj[0] - pi[0]
                jdy = pj[1] - pi[1]
                if (jdx <= 0 and jdy < 0) or jdx<0:
                    jdx, jdy = -jdx, -jdy

                div = gcd(jdx, jdy)
                dx, dy = jdx//div, jdy//div
                # print(f'({i:2d}, {j:2d}) = {dx=}, {dy=}')
                lines[(i,dx,dy)] = lines.get( (i,dx,dy), 0 ) + 1

        # for a,b in lines.items():
        #     print(f'{a}: {b}')


        lines[-1] = 0
        return 1+max(lines.values())

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.maxPoints,
        sol.maxPoints_count
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )


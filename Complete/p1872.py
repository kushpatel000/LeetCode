# 1872. Stone Game VIII
'''
Given a sequence of stones (each worth some integer value of points).

Each players turn is as follows:
  1. Remove 2 or more stones from the left
  2. Sum the points on the stones and add that to player score
  3. Add a new stone on the left equal to the score added

The game ends when there is only one stone left.

The final score difference is simply Alice - Bob

Alice (P1) wants to maximize the score difference.
Bob (P2) wants to minimize the score difference.

i.e. both players want to collect maximum points

-------------------------------------------------------------------------------
This feels like a dynamic-programming problem. 

Each step, the player will choose the maximum number of points take-able 
(minimum 2 stones). 
Further, at each step, they will inherently also take the number of points from
the previous step (adding the new stone back).


'''

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def __init__(self):
        self.player = 1
        self.level = ''

    def stoneGameVIII_greedy(self, stones: list[int]) -> int:
        cumul_points = [ stones[0] ]
        last_positive = 1 if stones[0] > 0 else -1

        for i,s in enumerate(stones[1:]):
            cumul_points.append( cumul_points[-1] + s )
            if cumul_points[-1] >= 0: last_positive = i+1

        # Step 1, Alice always takes the last postive cumulative points
        #   that way Bob never gets any positive value of points
        #   if there are no positive points, then choose the first two stones
        i = max(last_positive, 1)
        point_diff = cumul_points[i]
        # print(f'Alice chooses: {stones[:i+1]} for {cumul_points[i]} points')
        # Step 2, now there are only losing points
        #   each will take the least point loss at every step        

        side = -1

        while i < len(stones)-1:
            p = max(cumul_points[i+1:])
            j = cumul_points[i+1:].index(p) + i+1

            # print choices
            player = ['','Alice','Bob'][side]
            take = [cumul_points[i]] + stones[i+1:j+1]
            # print(f'{player} chooses {take} for {cumul_points[j]} points')

            # update 
            point_diff += side * p
            i = j
            side *= -1


        return point_diff

    def stoneGameVIII_recurse(self, stones: list[int]) -> int:
        # self.player = 1 - self.player
        # self.level += 'AB'[self.player]
        N = len(stones)
        if N < 2: return 0
        
        max_pts = sum(stones)

        for i in range(2, N):
            d = sum(stones[:i])
            new_stones = [d] + stones[i:]
            rm = self.stoneGameVIII_recurse( new_stones )
            # print(self.level, d, rm, stones[:i])
            max_pts = max( max_pts, d-rm )

        # self.level = self.level[:-1]
        # self.player = 1-self.player

        return max_pts

    def stoneGameVIII_dp(self, stones: list[int]) -> int:
        N = len(stones)
        CS = [stones[0]]
        for s in stones[1:]:
            CS.append(CS[-1] + s)
        
        best_delta = [CS[-1]] * N

        import tqdm
        for k in tqdm.trange(N-2,0,-1):
            for j in range(k,N-1):
                me = CS[j]
                opp = best_delta[j+1]
                best_delta[k] = max( best_delta[k], me - opp )
            # print(k, N)

        for k,(s,c,b) in enumerate(zip(stones, CS, best_delta)):
            print(f'{k:3d} | {s:3d} {c:3d} {b:3d}')
        
        return best_delta[1]
    
    def stoneGameVIII_dp2(self, stones: list[int]) -> int:
        N = len(stones)
        CS = [stones[0]]
        for s in stones[1:]:
            CS.append(CS[-1] + s)
        
        best_delta = [CS[-1]] * N

        import tqdm
        for k in tqdm.trange(N-2,0,-1):
            me = CS[k]
            opp = best_delta[k+1]
            best_delta[k] = max( best_delta[k], me-opp, opp )
            # for j in range(k,N-1):
            #     me = CS[j]
            #     opp = best_delta[j+1]
            #     best_delta[k] = max( best_delta[k], me - opp )
            # print(k, N)

        for k,(s,c,b) in enumerate(zip(stones, CS, best_delta)):
            print(f'{k:3d} | {s:3d} {c:3d} {b:3d}')
        
        return best_delta[1]


if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        # sol.stoneGameVIII_greedy,
        # sol.stoneGameVIII_recurse,
        # sol.stoneGameVIII_recurse2,
        # sol.stoneGameVIII_dp,
        sol.stoneGameVIII_dp2,
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,#[:-1],
        # [test_cases[3]],
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

    # import numpy as np
    # cumul_points = [-1,-2,-3,-4,-5]
    # N = len(cumul_points)
    # def traverse(last_take:int, side:int, takes:list, takers:list):
    #     # check end and print summary
    #     if last_take == N-1:
    #         for p in takes:
    #             print(f'{p:3d} ', end =' ')
    #         print()
    #         for t in takers:
    #             tk = {1:'A',-1:'B'}[t]
    #             print(f'{tk:^3s} ', end = ' ')
    #         print(f'\nPoint Delta: {np.dot(takes, takers)}')
    #         print()



    #         return

    #     # make takes
    #     for i in range(last_take+1, N):
    #         takes.append( cumul_points[i] )
    #         takers.append(side)
    #         traverse( i, -side, takes, takers)
    #         takes.pop()
    #         takers.pop()

    # traverse(-1, -1, [], [])

    # import pandas as pd
    # df = pd.DataFrame(
    #     sol.res,
    #     columns=['base','start','i','pts']
    # ).sort_values(by=['i','start'])

    # print(df[['i','pts']].drop_duplicates())
    # print(sol.best)
    # print(test_cases[3][0])
    # print(df.pts.max())
    
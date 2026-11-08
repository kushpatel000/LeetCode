# 0453. Minimum Moves to Equal Array Elements [Medium]
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/ 

from typing import List
import test_suite as ts

class Solution:
    def minMoves_naive(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        # print(f'{i:2d} {nums}')
        while nums[0] < nums[-1]:
            i += 1
            for k in range(len(nums)-1):
                nums[k] += 1
            nums.sort()
            # print(f'{i:2d} {nums}')
        return i

    def minMoves(self, nums: list[int]) -> int:
        M = min(nums)
        return sum(x - M for x in nums)



if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minMoves_naive,
        sol.minMoves
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

    # adding additional maxima increases the moves by a linear amount
    # - this increase is the maximum difference (max - min)
    # adding addtional medium values increases the count by (v - min)
    # adding additional minima does not change the count
    
    # is the solution sum(a - min(arr) for a in arr)?
    
    test = [5, 6 ,8 ,8, 5]
    for k in range(0,4):
        test_ = test + [5]*k
        mn = min(test_)
        test_res = sum(x - mn for x in test_)
        print(f'{test_} -> {sol.minMoves_naive(test_)}, {test_res}')


## Exploration  

'''
2 4 4 
2 5 4
3 5 5
4 6 5
5 6 6
6 7 6
7 7 7

initia information:
- we can only increment n-1 elements by 1 in each move
- min is 2
- max is 4
- delta is 2


It feels obvious that the

'''


#  // [
#     //     [1,1,1000000000],
#     //     999999999
#     // ],
   
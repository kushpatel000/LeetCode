# 1658. Minimum Operations to Reduce X to Zero


from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def minOperations_dfs(self, pack: list) -> int:
        nums, x = pack
        bad = len(nums)

        # base cases
        if sum(nums) < x: return -1
        if sum(nums) == x: return len(nums)

        @cache
        def dfs(curr, i, j, m):
            if curr == 0: return m

            if curr < 0 or i>j: return bad

            return min(
                dfs( curr - nums[i], i+1, j, m+1 ),
                dfs( curr - nums[j], i, j-1, m+1 )
            )
            
        res = dfs(x, 0, len(nums)-1, 0)
        if res < bad:
            return res
        return -1

    def minOperations(self, pack: list) -> int:
        nums, x = pack

        S = sum(nums)
        N = len(nums)
        # base cases
        if S < x: return -1
        if S == x: return N


        # if there is a solution, then there is a contiguous sub-array
        # of nums such that sum(sub_array) + x = sum(array)

        # want sum(sub_array) = sum(array)-x = target
        tgt = S-x
        i = 0
        j = 0
        sub_sum = 0
        soln = -1

        print(f'{tgt=}')

        while i < N and j <= N:
            assert sum(nums[i:j]) == sub_sum
        
            # update based on direction
            print(f'pre  {sub_sum=}, {i=}, {j=}')
            if sub_sum <= tgt:
                if j==N: break
                sub_sum += nums[j]
                j += 1
            else:
                sub_sum -= nums[i]
                i += 1
            print(f'post {sub_sum=}, {i=}, {j=}')

            # check if this is a solution
            if sub_sum == tgt:
                print('candidate:', i,j)
                l = nums[:i]
                r = nums[j:]
                print('  check', sum(l)+sum(r), x)
                print('  num:', len(l), len(r), len(l)+len(r), N-j+i)

                soln = max( soln, j-i )

        if soln == -1: return -1
        return len(nums) - soln


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minOperations_dfs,
        sol.minOperations,
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,#[-1:],
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

    # tc = test_cases[-1]
    # x = tc[0][1]
    # nums = tc[0][0]
    # print(nums)
    # n = len(nums)
    # print(f'{n=}')
    # ans = tc[1]
    # for i in range(ans):
    #     l = nums[:i]
    #     r = nums[i-n:]
    #     s = sum(l)+sum(r)

    #     print(f'{len(l):2d} {len(r):2d} {s:7d} {s==x}')


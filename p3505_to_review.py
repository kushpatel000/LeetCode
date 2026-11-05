# 3505. Minimum Operations to Make Elements Within K Subarrays Equal [Hard]
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/ 

from typing import List
import test_suite as ts

class Solution:
    def minOperations_sort(self, nums: List[int], x: int, k: int) -> int:
        '''
        x - subarray size
        k - number of subarrays
        '''

        def fast_median(arr:list) -> int:
            n = len(arr)
            return sorted(arr)[n//2]

        def print_matrix(mat):
            for row in mat:
                a = [f'{x:3.0f}' for x in row]
                print(', '.join(a).replace('inf', '   '))

        N = len(nums)
        S = N - x + 1
        sub_array_ops = list()
        to_median_ops = lambda arr,m: sum(abs(e-m) for e in arr)

        for i in range(S):
            sa = nums[i:i+x]
            sub_array_ops.append(to_median_ops(sa, fast_median(sa)))

        # dimensions S, k
        inf = float('inf')
        dp = [ [inf]*S for _ in range(k) ]

        # k = 0, choose this as the first one
        # what's the actual max C allowed for the first one?
        # all arrays account for x*k elements, so including c, there needs
        # to be that many elements
        # if N = 6 and we need 2 arrays of 3, then there needs to be 6 elements
        # N-0 = 6, N-1=5 (too small)

        '''
        N = 9, x = 3, k = 2
        c = 0 - 4 are allowed (including 4)
        [ 0, 1, 2, [3, 4, 5], 6, 7, 8 ]
        c can range from 0 to N - x*k, inclusive
        then the python range is:
            range(N - x*k + 1)
            range(S+x-1 - x*k + 1)
            range(S - x*(k-1))
        '''

        # only store the best option in each row
        dp[0][0] = sub_array_ops[0]
        for c in range(1, N-k*x+1):
            dp[0][c] = min(sub_array_ops[c], dp[0][c-1])
        # generalized
        for r in range(1,k):
            for c in range(r*x, N-(k-r)*x+1):
                dp[r][c] = min(sub_array_ops[c] + dp[r-1][c-x], dp[r][c-1])


        # print(f'[{N=}] {k=} sub-arrays of size {x=}')
        # print_matrix([nums, sub_array_ops])
        # print()

        # print_matrix(dp)
        return dp[-1][-1]

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        '''
        x - subarray size
        k - number of subarrays
        '''

        def fast_median(arr:list, i:int) -> int:
            # print(f'Find {i}th in {arr} ')
            if len(arr) == 1: return arr[0]

            pivot = arr[0]

            lo = [ e for e in arr if e <  pivot ]
            hi = [ e for e in arr if e >  pivot ]
            ps = [ e for e in arr if e == pivot ]

            if i < len(lo):
                return fast_median(lo, i)
            elif i < len(lo) + len(ps):
                return ps[0]
            else:
                return fast_median(hi, i - len(lo) - len(ps))


        def print_matrix(mat):
            for row in mat:
                a = [f'{x:3.0f}' for x in row]
                print(', '.join(a).replace('inf', '   '))

        N = len(nums)
        S = N - x + 1
        sub_array_ops = list()
        to_median_ops = lambda arr,m: sum(abs(e-m) for e in arr)

        for i in range(S):
            sa = nums[i:i+x]
            sub_array_ops.append(to_median_ops(sa, fast_median(sa, x//2)))

        # dimensions S, k
        inf = float('inf')
        dp = [ [inf]*S for _ in range(k) ]

        # only store the best option in each row
        dp[0][0] = sub_array_ops[0]
        for c in range(1, N-k*x+1):
            dp[0][c] = min(sub_array_ops[c], dp[0][c-1])
        # generalized
        for r in range(1,k):
            for c in range(r*x, N-(k-r)*x+1):
                dp[r][c] = min(sub_array_ops[c] + dp[r-1][c-x], dp[r][c-1])


        # print(f'[{N=}] {k=} sub-arrays of size {x=}')
        # print_matrix([nums, sub_array_ops])
        # print()

        # print_matrix(dp)
        return dp[-1][-1]
    
    def minOperations_arr(self, nums: List[int], x: int, k: int) -> int:
        '''
        x - subarray size
        k - number of subarrays
        '''

        def print_matrix(mat):
            for row in mat:
                a = [f'{x:3.0f}' for x in row]
                print(', '.join(a).replace('inf', '   '))

        N = len(nums)
        S = N - x + 1
        sub_array_ops = list()
        to_median_ops = lambda arr,m: sum(abs(e-m) for e in arr)

        import bisect
        # print(nums)
        sub_array = sorted(nums[:x-1])
        # print(sub_array)
        for i in range(x-1, N):
            bisect.insort( sub_array, nums[i] )
            # print(sub_array, to_median_ops(sub_array, sub_array[x//2]))
            sub_array_ops.append( to_median_ops(sub_array, sub_array[x//2]) )
            idx = bisect.bisect_left(sub_array, nums[i-x+1])
            # print(f'Removing {nums[i-x+1]} at index {idx}')
            sub_array.pop(idx)


            # return -1


        # dimensions S, k
        inf = float('inf')
        dp = [ [inf]*S for _ in range(k) ]

        # only store the best option in each row
        dp[0][0] = sub_array_ops[0]
        for c in range(1, N-k*x+1):
            dp[0][c] = min(sub_array_ops[c], dp[0][c-1])
        # generalized
        # import tqdm
        for r in range(1,k):
            for c in range(r*x, N-(k-r)*x+1):
                dp[r][c] = min(sub_array_ops[c] + dp[r-1][c-x], dp[r][c-1])


        # print(f'[{N=}] {k=} sub-arrays of size {x=}')
        # print_matrix([nums, sub_array_ops])
        # print()

        # print_matrix(dp)
        return dp[-1][-1]

    def editorial(self, nums: List[int], x: int, k: int) -> int:
        from collections import defaultdict
        from heapq import heappop, heappush
        inf = float('inf')

        n = len(nums)
        left, right = [], []
        delayed = defaultdict(int)
        left_size = right_size = 0
        sum_l = sum_r = 0
        ops = [0] * n

        def prune(h: List[int], sign: int) -> None:
            while h and delayed[sign * h[0]]:
                delayed[sign * h[0]] -= 1
                heappop(h)

        def balance() -> None:
            nonlocal left_size, right_size, sum_l, sum_r
            if left_size > right_size + 1:
                num = -heappop(left)
                heappush(right, num)
                sum_r += num
                sum_l -= num
                right_size += 1
                left_size -= 1
                prune(left, -1)
            elif right_size > left_size:
                num = heappop(right)
                heappush(left, -num)
                sum_l += num
                sum_r -= num
                left_size += 1
                right_size -= 1
                prune(right, 1)

        for i, num in enumerate(nums):
            if not left or num <= -left[0]:
                heappush(left, -num)
                left_size += 1
                sum_l += num
            else:
                heappush(right, num)
                right_size += 1
                sum_r += num
            balance()
            if i >= x:
                num = nums[i - x]
                delayed[num] += 1
                if num <= -left[0]:
                    left_size -= 1
                    sum_l -= num
                    if num == -left[0]:
                        prune(left, -1)
                else:
                    right_size -= 1
                    sum_r -= num
                    if num == right[0]:
                        prune(right, 1)
                balance()
            if i >= x - 1:
                mid = -left[0]
                ops[i] = sum_r - sum_l + mid * (left_size - right_size)

        dp = [[0] + [inf] * k for _ in range(n)]
        for j in range(1, k + 1):
            if j == 1:
                dp[x - 1][j] = ops[x - 1]
            else:
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + ops[j * x - 1]
        for j in range(1, k + 1):
            for i in range(j * x, n):
                dp[i][j] = min(dp[i - x][j - 1] + ops[i], dp[i - 1][j])
        return dp[n - 1][k]

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minOperations_sort,
        sol.minOperations,
        sol.minOperations_arr,
        sol.editorial
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[:-2],
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # a = [0,1,2,3,4]
    # b = a[:2]
    # print(f'{a=}')
    # print(f'{b=}')
    # b[0] = 5
    # print(f'{a=}')
    # print(f'{b=}')
        
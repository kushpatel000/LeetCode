# 2916. Subarrays Distinct Element Sum of Squares II [Hard]
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/ 

from typing import List
import test_suite as ts

import pandas as pd

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        M = 10**9 + 7
        N = len(nums)
        res = 0
        for i in range(N):
            elems = set()
            for j in range(i,N):
                elems.add(nums[j])
                res = (res + len(elems)**2) % M

        return res               

    def track_prev(self, nums: List[int]) -> int:
        '''
            This solution is from
            https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/solutions/8574693/snowball-subarrays-ii-fenwick-tree-onlog-fh7f
            I don't quite understand it yet
        '''
        M = 10**9 + 7
        N = len(nums)

        last_seen = {}
        res = 0

        for i, v in enumerate(nums):
            ls = last_seen.get(v, -1)
            last_seen[v] = i

            mult = N-i

            sub_res = (i-ls)**2
            
            if ls != -1:
                for q in range(ls, N):
                    if last_seen.get(nums[q],-1) > q:
                        sub_res -= 2*(q-ls)

            sub_res *= mult

            res = (res + sub_res) % M
            print(f'{i} - {sub_res} from {sub_res}')

            # last_seen[v] = i
        
        return res

    def FenwickTree(self, nums: List[int]) -> int:
        '''
        This solution is from
        https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/solutions/8574693/snowball-subarrays-ii-fenwick-tree-onlog-fh7f
        I don't quite understand it yet and it doesn't fully work
        '''
        n = len(nums)
        cnt, tot = [0] * (n + 1), [0] * (n + 1)  # Fenwick trees over previous-copy positions, stored right to left
        last, ans = {}, 0
        for r, x in enumerate(nums):
            p = last.get(x, -1)
            c = s = 0
            i = n - p - 1  # boxes 1..n-p-1 hold the positions > p
            while i:
                c += cnt[i]
                s += tot[i]
                i -= i & -i
            ans += (n - r) * ((r - p) ** 2 - 2 * (s - p * c))
            i = n - p  # insert p; p = -1 lands past the end and is skipped
            while i <= n:
                cnt[i] += 1
                tot[i] += p
                i += i & -i
            last[x] = r
        return ans % (10**9 + 7)

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.sumCounts   ,
        sol.track_prev
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[-1:],
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )

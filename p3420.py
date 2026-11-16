# 3420. Count Non-Decreasing Subarrays After K Operations [Hard]
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations 

#  You are given an array nums of n integers and an integer k.
#  For each subarray of nums, you can apply up to k operations on it. In each
#  operation, you increment any element of the subarray by 1.
#  Note that each subarray is considered independently, meaning changes made to one
#  subarray do not persist to another.
#  Return the number of subarrays that you can make non-decreasing ​​​​​after
#  performing at most k operations.
#  An array is said to be non-decreasing if each element is greater than or equal
#  to its previous element, if it exists.
#  Example 1:
#  Input: nums = [6,3,1,2,4,4], k = 7
#  Output: 17
#  Explanation:
#  Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3,
#  1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing
#  after applying up to k = 7 operations. Thus, the number of non-decreasing
#  subarrays is 21 - 4 = 17.
#  Example 2:
#  Input: nums = [6,3,1,3,6], k = 4
#  Output: 12
#  Explanation:
#  The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer
#  elements, except [6, 3, 1], can be made non-decreasing after k operations. There
#  are 5 subarrays of a single element, 4 subarrays of two elements, and 2
#  subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12
#  subarrays that can be made non-decreasing.
#  Constraints:
#  1 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^9
#  1 <= k <= 10^9

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

from collections import defaultdict, deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # print(f'{k=} {nums=}')
        sp = defaultdict(dict)
        # sp[start][stop] = (cumul max, cumul moves)

        N = len(nums)
        for i in range(N-1):
            sp[i][i+1] = ( max(nums[i:i+2]), max(nums[i]-nums[i+1], 0) ) 
            for j in range(i+2, N):
                cm, cp = sp[i][j-1]
                cm = max( cm, nums[j] )
                cp = cp + (cm-nums[j])
                sp[i][j] = (cm, cp)

            # print(f'{i=}')
            # for j in sp[i].keys():
            #     print(f'  {j=}:{sp[i][j]}')

        count = 0
        for i,v in sp.items():
            count += 1
            # print(f'{count:2d} -- ({i},  ) -- {nums[i:i+1]}')
            for j,(m,p) in v.items():
                if p <= k:
                    count += 1
                    # print(f'{count:2d} -- ({i}, {j}) -- <<{m:2d}>> {nums[i:j+1]}')
                # else:
                #     print(f'XX -- ({i}, {j}) -- <<{p:2d}>> {nums[i:j+1]}')
            # count += sum([a for a in v.values() if a <= k])

        # print(f'{count=}')
        return count+1

    def countNonDecreasingSubarrays_2(self, nums: List[int], k: int) -> int:
        N = len(nums)
        counts = 0
        for i in range(N):
            cm, cp = 0, 0
            for j in range(i, N):
                cm = max(cm, nums[j])
                cp += cm - nums[j]
                if cp > k:
                    # print(f'X {i}->{j}: {nums[i:j+1]}')
                    break
                else:
                    # print(f'  {i}->{j}: {nums[i:j+1]}')
                    counts += 1

            # counts += j-i+1
            # print(counts)
        return counts

    def aleksandr(self, nums: List[int], k: int) -> int:
        starts = deque()  # where each plateau starts, left to right
        ans, water, r = 0, 0, len(nums) - 1
        for l in reversed(range(len(nums))):
            x = nums[l]
            while starts and nums[starts[0]] <= x:  # x floods the plateau that starts at starts[0]
                s = starts.popleft()
                end = starts[0] if starts else r + 1
                water += (x - nums[s]) * (end - s)
            starts.appendleft(l)
            while water > k:  # the right end leaves with its water
                water -= nums[starts[-1]] - nums[r]
                if starts[-1] == r:
                    starts.pop()
                r -= 1
            ans += r - l + 1
        return ans

        

if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.countNonDecreasingSubarrays,
        sol.countNonDecreasingSubarrays_2,
        sol.aleksandr
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
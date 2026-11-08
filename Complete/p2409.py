# 2409. Count Days Spent Together [Easy]
# https://leetcode.com/problems/count-days-spent-together/ 

from typing import List
import test_suite as ts

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def extract_date_of_year(word:str):
            month, day = word.split('-')
            month = int(month)
            return sum(num_days[:month-1]) + int(day)

        aa, la, ab, lb = map(extract_date_of_year, [arriveAlice, leaveAlice, arriveBob, leaveBob])

        last_arrive = max(aa, ab)
        first_leave = min(la, lb)
        return max(first_leave - last_arrive + 1, 0)


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.countDaysTogether
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )
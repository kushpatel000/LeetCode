# 2124. Check if All A's Appears Before All B's [Easy]
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs 

#  Given a string s consisting of only the characters 'a' and 'b', return true if
#  every 'a' appears before every 'b' in the string. Otherwise, return false.
#  Example 1:
#  Input: s = "aaabbb"
#  Output: true
#  Explanation:
#  The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
#  Hence, every 'a' appears before every 'b' and we return true.
#  Example 2:
#  Input: s = "abab"
#  Output: false
#  Explanation:
#  There is an 'a' at index 2 and a 'b' at index 1.
#  Hence, not every 'a' appears before every 'b' and we return false.
#  Example 3:
#  Input: s = "bbb"
#  Output: true
#  Explanation:
#  There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
#  Constraints:
#  1 <= s.length <= 100
#  s[i] is either 'a' or 'b'.

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:
    def checkString(self, s: str) -> bool:
        first_b = s.find('b')  
        first_a = s[::-1].find('a')

        if first_b == -1 or first_a == -1:
            return True

        first_a = len(s) - first_a - 1
        return first_a < first_b

    def checkString_2(self, s:str) -> bool:
        return 'ba' not in s


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.checkString,
        sol.checkString_2,
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )
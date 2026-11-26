# 3360. Stone Removal Game [Easy]
# https://leetcode.com/problems/stone-removal-game 

#  Alice and Bob are playing a game where they take turns removing stones from a
#  pile, with Alice going first.
#  Alice starts by removing exactly 10 stones on her first turn.
#  For each subsequent turn, each player removes exactly 1 fewer stone than the
#  previous opponent.
#  The player who cannot make a move loses the game.
#  Given a positive integer n, return true if Alice wins the game and false
#  otherwise.
#  Example 1:
#  Input: n = 12
#  Output: true
#  Explanation:
#  Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
#  Bob cannot remove 9 stones, so Alice wins.
#  Example 2:
#  Input: n = 1
#  Output: false
#  Explanation:
#  Alice cannot remove 10 stones, so Alice loses.
#  Constraints:
#  1 <= n <= 50

###############################################################################
###############################################################################

from typing import List
import test_suite as ts

class Solution:
    def canAliceWin(self, n: int) -> bool:
        # this problem is very constrained (n <= 50), so we can use recursion
        def can_win(m:int, r:int):
            if m < r:
                return False
            return not can_win(m-r, r-1)

        return can_win(n, 10)

    def hard_code(self, n:int) -> bool:
        return n in {
            10,11,12,13,14,15,16,17,18,
            27,28,29,30,31,32,33,
            40,41,42,43,44,
            49,50
        }


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.canAliceWin,
        sol.hard_code
    ]

    test_cases = ts.load_test_cases(__file__)

    # ts.test_all(
    #     test_cases,
    #     test_funcs,
    #     # check_thresh = 1e-5,
    #     # display = True,
    #     # test_only = True
    # )

    for k in range(1,51):
        print(f'{k:2d} - {sol.canAliceWin(k)}, {sol.hard_code(k)}')
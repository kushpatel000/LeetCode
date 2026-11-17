# 2911. Minimum Changes to Make K Semi-palindromes [Hard]
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes 

#  Given a string s and an integer k, partition s into k substrings such that the
#  letter changes needed to make each substring a semi-palindrome are minimized.
#  Return the minimum number of letter changes required.
#  A semi-palindrome is a special type of string that can be divided into
#  palindromes based on a repeating pattern. To check if a string is a semi-
#  palindrome:​

#  Choose a positive divisor d of the string's length. d can range from 1 up to,
#  but not including, the string's length. For a string of length 1, it does not
#  have a valid divisor as per this definition, since the only divisor is its
#  length, which is not allowed.

#  For a given divisor d, divide the string into groups where each group contains
#  characters from the string that follow a repeating pattern of length d.
#  Specifically, the first group consists of characters at positions 1, 1 + d, 1 +
#  2d, and so on; the second group includes characters at positions 2, 2 + d, 2 +
#  2d, etc.

#  The string is considered a semi-palindrome if each of these groups forms a
#  palindrome.
#  Consider the string "abcabc":
#  The length of "abcabc" is 6. Valid divisors are 1, 2, and 3.
#  For d = 1: The entire string "abcabc" forms one group. Not a palindrome.
#  For d = 2:
#  Group 1 (positions 1, 3, 5): "acb"
#  Group 2 (positions 2, 4, 6): "bac"
#  Neither group forms a palindrome.
#  For d = 3:
#  Group 1 (positions 1, 4): "aa"
#  Group 2 (positions 2, 5): "bb"
#  Group 3 (positions 3, 6): "cc"
#  All groups form palindromes. Therefore, "abcabc" is a semi-palindrome.
#  Example 1:
#  Input:   s = "abcac", k = 2
#  Output:   1
#  Explanation:  Divide s into "ab" and "cac". "cac" is already semi-palindrome.
#  Change "ab" to "aa", it becomes semi-palindrome with d = 1.
#  Example 2:
#  Input:   s = "abcdef", k = 2
#  Output:   2
#  Explanation:  Divide s into substrings "abc" and "def". Each needs one change to
#  become semi-palindrome.
#  Example 3:
#  Input:   s = "aabbaa", k = 3
#  Output:   0
#  Explanation:  Divide s into substrings "aa", "bb" and "aa". All are already
#  semi-palindromes.
#  Constraints:
#  2 <= s.length <= 200
#  1 <= k <= s.length / 2
#  s contains only lowercase English letters.


###############################################################################
# Hint 1
#   Define dp[i][j] as the minimum count of letter changes needed to split the 
#   suffix of string s starting from s[i] into j valid parts.
# Hint 2
#   We have dp[i][j] = min(dp[x + 1][j - 1] + v[i][x]). Here v[i][x] is the 
#   minimum number of letter changes to change substring s[i..x] into 
#   semi-palindrome.
# Hint 3
#   v[i][j] can be calculated separately by brute-force. We can create a table 
#   of v[i][j] independently to improve the complexity. Also note that 
#   semi-palindrome’s length is at least 2.

###############################################################################
###############################################################################

from typing import List, Iterable
import test_suite as ts
from functools import cache

class Solution:
    def minimumChanges_naive(self, s: str, k: int) -> int:
        INF = float('inf')
        # step 1 - choose a split
        def split(phr:str, n: int) -> int:
            if len(phr) == 1: return INF

            space = k-n+2
            
            if n == 1:
                # print(' '*space + f'Processing "{phr}"')
                return min([
                    sum([ num_ops(g) for g in make_groups(phr, d) ])
                    for d in get_divisors(len(phr))
                ])
                
            M = INF
            for i in range(1, len(phr)-1):
                # print(' '*space + f'{n=} Splitting "{phr[:i]}|{phr[i:]}"')
                L = split( phr[:i], 1 )
                # if L >= M: continue
                R = split( phr[i:], n-1 )
                M = min(M, L+R)
            return M

        # step 2 - for each substring in the split, iterate through divisors
        def get_divisors(n:int) -> List[int]:
            return [i for i in range(1,n) if n%i==0]
        
        # step 3 - for each divisor, split the substring into the groups
        def make_groups(substr:str, d:int) -> List[str]:
            if d == len(substr):
                raise ValueError(f'Invalid divisor size: {d},')
            arr = [ substr[i:i+d] for i in range(0, len(substr), d) ]
            return list(zip(*arr))

        # step 4 - for each group, determine the number of swaps needed to 
        #          make the group a palindrome
        def num_ops(phr:Iterable) -> int:
            if len(phr) == 1: return 0
            return sum([ phr[i]!=phr[-i-1] for i in range(len(phr)//2) ])



        # print(f'Header: {s=}, {k=}')
        return split(s, k)

    
    def minimumChanges(self, s: str, k: int) -> int:
        # params ##############
        INF = float('inf')
        N = len(s)

        # funcs ###############
        @cache
        def get_divisors(n:int) -> List[int]:
            return [i for i in range(1,n) if n%i==0]

        @cache                
        def num_ops(phr:Iterable) -> int:
            if len(phr) == 1: return 0
            return sum([ phr[i]!=phr[-i-1] for i in range(len(phr)//2) ])

        
        @cache
        def v(i:int,x:int) -> int:
            # How many steps to turn s[i:x+1] into a semi-palindrome?

            substr = s[i:x+1]
            return min([
                sum([ num_ops(substr[i::d]) for i in range(d) ])
                for d in get_divisors(x+1-i)
            ])
            
        # process #############
        dp = [ [INF]*k for _ in s ]

        for i in range(N-1, -1, -1):
            for j in range(1, k+1):
                print(f'{s=}, {i=}, {j=}')
                if N-i >= j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[x + 1][j - 1] + v(i,x) for x in range(i,N-2))

        for row in dp:
            print(row)




if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.minimumChanges_naive,
        sol.minimumChanges
    ]

    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases[:-1],
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


'''

aabbaa

d = 1
groups = [aabbaa]
>> All palindromes, zero ops

_groups = [0,1,2,3,4,5]
compare: 0,5 ; 1,4 ; 2,3
[i,x], work inward, iterate 1

d = 2
groups = [aba, aba] 
>> All palindromes, zero ops

_groups = [0,2,4], [1,3,5]
compare: 0,4, ; 1,5


d = 3
groups = [ab, aa, ba]
>> 2 operations are necessary

_groups = [0,3], [1,4], [2,5]
compare: 0,3 ; 1,4 ; 2,5



'''
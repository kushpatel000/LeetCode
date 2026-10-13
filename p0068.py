# 0068. Text Justification

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []

        curr_line = []
        curr_len = 0

        for w in words:
            # check if adding this word would exceed the maxWidth
            if curr_len + len(curr_line) + len(w) > maxWidth:
                # process this line
                add_spaces = maxWidth - curr_len

                if len(curr_line) == 1:
                    lines.append(curr_line[0] + ' '*add_spaces)
                else:
                    per_word, extra = divmod(add_spaces, len(curr_line)-1) if len(curr_line) > 1 else (0, add_spaces)
                    for i in range(extra):
                        curr_line[i] += ' '
                    lines.append( (' '*per_word).join(curr_line) )
                
                
                print(f'[{lines[-1]}]')
                
                # reset
                curr_line = []
                curr_len = 0
            
            curr_line.append(w)
            curr_len += len(w)
            print(curr_len, curr_line)

        # add the last line
        L = ' '.join(curr_line)
        L = L + ' '*(maxWidth - len(L))
        print(f'[{L}]')
        lines.append(L)

        return lines

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.fullJustify,
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


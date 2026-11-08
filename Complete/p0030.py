# 0030. Substring with Concatentaion of All Words

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        Assume all words are of the same length and unique.
        '''
        W = len(words[0])
        L = len(words) * W
        
        word_counts = dict()
        for w in words:
            word_counts[w] = word_counts.get(w, 0) + 1
        
        print(f'{W=}, {L=}')
        print(word_counts)

        def count_words(ss:str) -> dict:
            counts = dict()
            for k in range(0, len(ss), W):
                w = ss[k:k+W]
                counts[w] = counts.get(w, 0) + 1
            return counts

        
        results = list()
        for k in range(0, len(s)-L+1):
            substr = s[k:k+L]
            counts = count_words(substr)
            if counts == word_counts:
                results.append(k)
            print(' '.join([substr[i:i+W] for i in range(0, len(substr), W)])  )
            print()

        return results
    

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.findSubstring
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        display = True,
        test_only = True
    )


    # import inspect
    # for func in test_funcs:
    #     print(func.__name__)
    #     # get the number of arguments the function takes
    #     sig = inspect.signature(func)
    #     n_args = len(sig.parameters)
    #     print(n_args)
    #     print(sig.parameters)
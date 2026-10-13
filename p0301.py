# 0301. Remove Invalid Parentheses

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def removeInvalidParentheses_recurse(self, s: str) -> list[str]:

        def traverse(
            curr_str:str, 
            next_idx:int, 
            depth:int, 
            results:list
        ) -> list[str]:
            # base checks
            if depth < 0: return results
            if depth > len(s) - next_idx: return results

            # check if this is the end
            if next_idx == len(s):
                # no result
                if depth != 0: return results
                # print(depth, curr_str)

                if len(results) == 0:
                    results.append(curr_str)
                elif len(curr_str) == len(results[0]):
                    results.append(curr_str)
                elif len(curr_str) > len(results[0]):
                    results = [curr_str]
                
                return results


            choose = curr_str + s[next_idx]
            new_depth = depth + {'(':1, ')':-1}.get(s[next_idx], 0)
            
            results = traverse(curr_str, next_idx+1, depth, results)
            results = traverse(choose, next_idx+1, new_depth, results)
            return results



        results = traverse('', 0, 0, [])
        return sorted(set(results))

    def removeInvalidParentheses_iterate(self, s: str) -> list[str]:

        def valid(t):
            d = 0
            for c in t:
                if c == '(':
                    d += 1
                elif c == ')':
                    d -= 1
                    if d < 0: return False
            return d==0


        curr_set = set([s])
        result = list()

        while curr_set:
            for test in curr_set:
                if valid(test):
                    result.append(test)

            if result: break


            new_set = set()
            for test in curr_set:
                prev_c = ''
                for i,c in enumerate(test):
                    if c == prev_c: continue
                    
                    prev_c = c
                    if c in '()':
                        new_set.add( test[:i]+test[i+1:] )

            curr_set = new_set

        return sorted(result)


    def removeInvalidParentheses_iterate2(self, s: str) -> list[str]:
        def valid(t):
            d = 0
            for c in t:
                if c == '(':
                    d += 1
                elif c == ')':
                    d -= 1
                    if d < 0: return False
            return d==0


        curr_set = set([s])
        result = list()

        while curr_set:
            result = [ test for test in curr_set if valid(test)]
            if result: return sorted(result)


            new_set = set()
            for test in curr_set:
                prev_c = ''
                for i,c in enumerate(test):
                    if c == prev_c: continue
                    
                    prev_c = c
                    if c in '()':
                        new_set.add( test[:i]+test[i+1:] )

            curr_set = new_set

        return ['']
        
if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        sol.removeInvalidParentheses_recurse,
        sol.removeInvalidParentheses_iterate2,
        sol.removeInvalidParentheses_iterate,
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

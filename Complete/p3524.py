# 3525. Find X Value of Array II


from functools import cache
from typing import List
import test_suite as ts


class Solution:
    # def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
    def resultArray(self, pack) -> List[int]:
        nums, k, queries = pack
        
        res = [0] * len(queries)

        for j,(i,v,s,x) in enumerate(queries):
            nums[i] = v

            cumprod_mod = 1
            for l, n in enumerate(nums[s:]):
                cumprod_mod = (cumprod_mod * n) % k 

                if cumprod_mod == 0:
                    if x == 0:
                        res[j] = len(nums)-s-l
                    break

                res[j] += (cumprod_mod == x)
                
        return res

    def resultArray_segtree(self, pack) -> List[int]:
        nums, k, queries = pack
        print(f'{k=}')
        N = len(nums)
        res = [0] * len(queries)

        size = len( f'{N-1:b}' )+1
        segtree_size = 2**(size) - 1 
        P = 2**(size-1)-1

        print(f'{N=} {size=} {segtree_size=}')

        # root of tree
        # 1 is idempotent with product, so let that be the default
        segtree = [1]*segtree_size

        def _update_parents(i):
            if i == 0: return
            p = (i-1) // 2
            segtree[p] = (segtree[2*p+1] * segtree[2*p+2]) #% k
            # print(f'{i=:2d} {p=:2d} l={2*p+1:2d} r={2*p+2:2d} s[{p}]={segtree[p]:d}')
            _update_parents(p)

        for i, n in enumerate(nums):
            segtree[P+i] = n #% k
            _update_parents(P+i)

        print(segtree)
        for j,(i,v,s,x) in enumerate(queries):
            print(f'{i=} i`={P+i} {v=} {s=} {x=}')
            segtree[P+i] = v #% k
            _update_parents(P+i)



            break

        print(segtree)
        print(nums)
        return res

    
if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        sol.resultArray,
        sol.resultArray_segtree,
    ]

    test_cases = ts.load_test_cases(__file__)

    # ts.test_all(
    #     test_cases[:1],
    #     test_funcs,
    #     # check_thresh = 1e-5,
    #     display = True,
    #     test_only = True
    # )

    sol.resultArray_segtree(
        test_cases[0][0]
    )

    # for N in [5,10,8,16,14]:
    #     size = len( f'{N-1:b}' )+1
    #     segtree_size = 2**(size)

    #     print(f'{N=:4d} {size=:2d} {segtree_size=:5d}')
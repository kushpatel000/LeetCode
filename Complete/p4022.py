# 4022. <Problem Name>

from functools import cache
from typing import List
import test_suite as ts

class Solution:
    def kthDigit_brute(self, k:int) -> int:
        string = ''
        for b in range(500):
            s, f = 10*b, 10*b+9
            if b%2 == 1:
                for n in range(f, s-1, -1):
                    string += str(n)
            else:
                for n in range(s, f+1):
                    string += str(n)

            if len(string) > k:
                # print(f'{k=}, {b=}')
                break

        # if k > 20:
        #     N = len(string)
        #     print(string[:10])
        #     this_line = k - 10
        #     for d in range(10, N, 20):
        #         print(string[d:d+20])
        #         if this_line < 20:
        #             print(' '*this_line + '^')
        #             break
        #         this_line -= 20


        return int(string[k])

    def kthDigit(self, k:int) -> int:
        if k < 10: return k

        # block0 = 9 # == 9*1
        # block9 = 180 # == 90 * 2 
        # block99 = 2700 # == 900 * 3
        # block999 = 36_000 # == 9000 * 4

        # calculate the block number
        b = 1
        i = k-10
        for m in range(2,16):
            # all digits in this magnitude are as:
            max_digits = 9 * m * 10**(m-1)
            # if there are more than the max number of digits, we can skip this magnitude
            if i > max_digits:
                i -= max_digits
                # total blocks are max_digits / m / 10
                b += 9 * 10**(m-2)
            else:
                # each block of 10 in magnitude /m/ has m*10 digits
                # how many whole blocks of this magnitude are before k?
                d,i = divmod(i, 10*m)
                b += d
                # print(f'{m=} | {d=}, {i=}')
                break

        # print(f'{b=}, {i=}')

        
        s, f = 10*b, 10*b+9
        # print(f'{s=}, {f=}')
        if b % 2 == 0:
            block_string = ''.join([ str(i) for i in range(s,f+1) ])
        else:
            block_string = ''.join([ str(i) for i in range(f,s-1, -1) ])

        # if k > 20:
        #     cumul_digs = 0
        #     for b in range(9):
        #         string = ''
        #         s, f = 10*b, 10*b+9
        #         if b%2 == 1:
        #             for n in range(f, s-1, -1):
        #                 string += str(n)
        #         else:
        #             for n in range(s, f+1):
        #                 string += str(n)
        #         cumul_digs += len(string)
        #         print(f'{b=:d} {cumul_digs:5,d} > {string}')

        # print(block_string)
        # a_, b_ = divmod(i,m)
        # marker = ' '*(m-1) + '*'
        # for _ in range(a_):
        #     print(marker, end='')
        # print(' '*b_ + '^')
        return int(block_string[i])


    def kthDigit_A(self, k:int) -> int:
        if k < 10: return k

        k -= 10
        # get the relevent magnitude
        m = 2
        b = 1
        while True:
            max_digits = 9 * m * 10**(m-1)
            # print(f'{m=}, {max_digits=}')
            if k >= max_digits:
                k -= max_digits
                b += 9 * 10**(m-2)
                m += 1
                # print(f'  {k=}, {b=}')
            else: 
                break

        # now find which block it belongs to
        d, r = divmod(k, 10*m)
        b += d
        # print(f'{m=}, {b=}, {r=}')

        n, g = divmod(r, m)
        g = m-g-1
        if b % 2 == 1: n=9-n

        l = 10*b + n
        # print(f'  {n=}, {g=}, {l=}')
        return (l % 10**(g+1)) // 10**g

    
    def kthDigit_B(self, k:int) -> int:
            if k < 10: return k
    
            k -= 10
            # get the relevent magnitude
            m = 2
            b = 1
            while True:
                max_digits = 9 * m * 10**(m-1)
                # print(f'{m=}, {max_digits=}')
                if k > max_digits:
                    k -= max_digits
                    b += 9 * 10**(m-2)
                    m += 1
                    # print(f'  {k=}, {b=}')
                else: 
                    break
    
            # now find which block it belongs to
            d, r = divmod(k, 10*m)
            b += d
            # print(f'{m=}, {b=}, {r=}')
    
            # # generate the block's string and return the digit
            # s, f = 10*b, 10*b+9
            # if b % 2 == 0:
            #     block_string = ''.join([ str(i) for i in range(s,f+1) ])
            # else:
            #     block_string = ''.join([ str(i) for i in range(f,s-1, -1) ])
            # return int(block_string[r])
    
            n, g = divmod(r, m)
            g = m-g-1
            if b % 2 == 1: n=9-n

            if g == m-1: return n
            # if g == 0: return n

            return int(str(b)[g-1])
            l = 10*b + n
    
            return (l % 10**(g+1)) // 10**g
    
    

if __name__ == "__main__":
    print('\n'*10)
    sol = Solution()

    test_funcs = [
        # sol.kthDigit_brute,
        sol.kthDigit,
        sol.kthDigit_A,
        # sol.kthDigit_B,
    ]
    
    test_cases = ts.load_test_cases(__file__)

    ts.test_all(
        test_cases,
        test_funcs,
        # check_thresh = 1e-5,
        # display = True,
        # test_only = True
    )

    # a = []
    # b = []

    # for m in range(5):
    #     a.append( 9 * 10**m * (m+1) )

    #     res = ''
    #     for k in range(10**m, 10**(m+1)):
    #         res += str(k)
    #     b.append(len(res))

    # for aa,bb in zip(a,b):
    #     print(f'{aa} {bb} {aa==bb}')
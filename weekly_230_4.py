from functools import cache
from typing import List
import test_suite as ts
import heapq
import tqdm

class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        nc = len(cars)
        cts = [-1] * nc

        # add the index
        for i in range(nc):
            cars[i].append(i)
            
        current_time = 0
        with tqdm.tqdm(total=nc) as pbar:
            while True:
                # find the smallest collision time
                next_ct = 1e7
                next_ct_idcs = list()
            
                for i in range(len(cars)-1):
                    # if car is faster than the next car
                    if cars[i][1] > cars[i+1][1]:
                        dd = cars[i+1][0] - cars[i][0]
                        dv = cars[i][1] - cars[i+1][1]
                        dt = dd/dv
                        if dt == next_ct:
                            next_ct_idcs.append(i)
                        elif dt < next_ct:
                            next_ct_idcs = [i]
                            next_ct = dt

                # no more collisions
                if len(next_ct_idcs) == 0: break
                
                # advance time
                current_time += next_ct
                
                # print(f'{next_ct=}')
                # print(f'{next_ct_idcs=}')
                # print(f'{current_time=}')
                # print(f'{cts=}')
                # print(cars)
                
                # update positions
                for i in range(len(cars)):
                    cars[i][0] += cars[i][1] * next_ct
                    
                # pop colliding cars and log time
                while next_ct_idcs:
                    C = cars.pop( next_ct_idcs.pop() )
                    cts[ C[2] ] = current_time
                
                pbar.set_postfix(current_val = len(cars))
            # if len(cts) > 2000:
            #     print(f'n_cars = {len(cars):7,d}' )

        return cts

    def _heap_print(self, h:list, i:int=0):
        if i == 0: print('Ordered Heap')
        if i < len(h):
            print( f'{h[i][0]:6.3f} {-h[i][1]:4d}' )
            self._heap_print(h, 2*i+1)
            self._heap_print(h, 2*i+2)

    def _print_cars(self, cars:list):
        print('== Cars ==')
        for c in cars:
            print(f'x={c[0]} v={c[1]}')

    def getCollisionTimes_v2(self, cars: list[list[int]]) -> list[float]:
        nc = len(cars)
        cts = [-1] * nc
        lead_car = [k+1 for k in range(nc-1)]

        def calc_collision_time(ca, cb) -> float:
            dd = cb[0] - ca[0]
            dv = ca[1] - cb[1]
            if dv <= 0: return 1e7

            dt = dd/dv
            return dt

        for i in tqdm.tqdm(range(nc-2, -1, -1)):
            first_col = 1e7
            col_car_idx = i

            next_car = lead_car[i]
            dt = calc_collision_time(cars[i], cars[next_car]) 
            if dt < first_col:
                first_col = dt
                col_car_idx = next_car
                
            while 0 < cts[next_car] < dt :
                next_car = lead_car[next_car]
                dt = calc_collision_time(cars[i], cars[next_car]) 
                if dt < first_col:
                    first_col = dt
                    col_car_idx = next_car

            if col_car_idx != i:
                cts[i] = first_col
                lead_car[i] = col_car_idx

        return cts


if __name__ == '__main__':
    print('\n'*10)


    sol = Solution()

    test_funcs = [
        # sol.getCollisionTimes,
        sol.getCollisionTimes_v2,
    ]

    test_cases = ts.load_test_cases(__file__)

    # ts.test_all(
    #     test_cases,
    #     test_funcs,
    #     check_thresh = 1e-5,
    #     # display = True,
    #     # test_only = True
    # )

    ts.check_soln(
        sol.getCollisionTimes_v2,
        *test_cases[5],
        ts._make_validation_func(1e-5, test_cases[0][1]),
        display=True
    )

    # res = sol.getCollisionTimes_v2(cars=test_cases[2][0])

    # min_incorrect = max(res)
    # min_incorrect_idx = len(res)
    
    # for i,(a,b) in enumerate(zip(res, test_cases[2][1])):
    #     close = abs(a-b)<10e-5
    #     if not close or 798 < i < 805:
    #         print(f'{i:4d} {a:10.4f} {b:10.4f}')

    #         if b < min_incorrect:
    #             min_incorrect = b
    #             min_incorrect_idx = i

    # print(f'Check this car: {min_incorrect_idx}')
    # print('')

    # print(res)
    # print(test_cases[2][1])
    

    # for tc in test_cases:
    #     print(len(tc[0]))

    # print(type(__file__))

    # print(ts.load_test_cases(__file__))

    # for c in test_cases[-1][0][-20:]:
    #     print(f'{c[0]:9,d} {c[1]:9,d}')
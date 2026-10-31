
import timeit
from typing import List


def get_times(func, args, repeat:int=5, number:int=100):

    time_results = timeit.repeat(
        lambda: func(args),
        repeat=repeat,
        number=number
    )

    return min(time_results)




def construct_then_populate(nums:List[int]) -> List[int]:
    n = len(nums)//2
    res = [0] * len(nums)
    # for i in range(0, 2*n, 2):
    #     a,b = 

    # for i, (a,b) in enumerate(zip( nums[:n], nums[n:] )):
    #     res[2*i] = a
    #     res[2*i+1] = b

    for i in range(n):
        res[2*i] = nums[i]
        res[2*i+1] = nums[i+n]

    return res


def just_extend(nums:List[int]) -> List[int]:
    n = len(nums)//2
    res = list()
    for a,b in zip( nums[:n], nums[n:] ):
        res.extend([a,b])

    return res



def main():
    funcs = [
        construct_then_populate,
        just_extend
    ]

    test_case = list(range(10000))

    for f in funcs:
        t = get_times(f, test_case, repeat=10, number=1000)
        if t < 1e-3:
            print(f'{t:6.3e} {f.__name__}')
        else:
            print(f'{t:6.3f} {f.__name__}')








    

if __name__ == '__main__':
    main()
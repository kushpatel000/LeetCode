
import timeit
from typing import List


def get_times(func, args, repeat:int=5, number:int=100):

    time_results = timeit.repeat(
        lambda: func(args),
        repeat=repeat,
        number=number
    )

    return min(time_results)




# def construct_then_populate(nums:List[int]) -> List[int]:
#     n = len(nums)//2
#     res = [0] * len(nums)
#     # for i in range(0, 2*n, 2):
#     #     a,b = 

#     # for i, (a,b) in enumerate(zip( nums[:n], nums[n:] )):
#     #     res[2*i] = a
#     #     res[2*i+1] = b

#     for i in range(n):
#         res[2*i] = nums[i]
#         res[2*i+1] = nums[i+n]

#     return res


# def just_extend(nums:List[int]) -> List[int]:
#     n = len(nums)//2
#     res = list()
#     for a,b in zip( nums[:n], nums[n:] ):
#         res.extend([a,b])

#     return res

def instantiate_and_populate(n:int) -> List[int]:
    a = [0]*n
    for i in range(n):
        a[i] = i
    return a

def append_from_empty(n:int) -> List[int]:
    a = list()
    for i in range(n):
        a.append(i)
    return a



def main():
    funcs = [
        # construct_then_populate,
        # just_extend

        instantiate_and_populate,
        append_from_empty
    ]

    test_case = 1000

    for f in funcs:
        t = get_times(f, test_case, repeat=10, number=10000)
        if t < 1e-2:
            print(f'{t:6.3e} {f.__name__}')
        else:
            print(f'{t:6.3f} {f.__name__}')








    

if __name__ == '__main__':
    main()
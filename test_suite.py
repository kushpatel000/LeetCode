from typing import List, Tuple
import time
import timeit
import tqdm
from collections.abc import Iterable
import numpy as np
from pathlib import Path
import json
from copy import deepcopy
import inspect

def load_test_cases(path:Path|str) -> List:
    path = Path(path)
    test_case_file = path.parent / f'Test_Cases/{path.stem}.json'
    return json.loads(test_case_file.read_text())

def _truncated_print(v, lim:int=80) -> None:
    vs = str(v)
    if len(vs) < lim:
        print(vs)
    else:
        print(vs[:lim] + ' ...')

def eval_input(inp):
    if isinstance(inp, str) and inp.startswith('eval~~'):
        return eval( inp.removeprefix('eval~~') )
    return inp

def check_soln(
    func,
    inp,
    out,
    validation_func,
    nargs:int,
    display:bool=False
) -> bool:
    inp_e = eval_input(inp)
    # validate the results
    inp_e = eval_input(inp)
    result = func( deepcopy(inp_e) ) if nargs == 1 else func( *deepcopy(inp_e) )
    success = validation_func(result, out)
    
    if display:
        print(f'Calculated Output [{func.__name__}]')
        _truncated_print(result)
        if success:
            print('✅ Test Passed')
        else:
            print('❌ Test Failed - Expected Output')
            _truncated_print(out)
        print()

    return success
    
def time_soln(
    func,
    inp,
    display,
    nargs:int,
    repeat:int = 5,
    number:int = 1000
) -> Tuple[float, bool]:

    inp_e = eval_input(inp)
    
    time_results = timeit.repeat(
        lambda: func(inp_e) if nargs == 1 else func(*inp_e),
        number=10000,
        repeat=repeat
    )
    best_time = min(time_results)

    if display:
        if best_time < 1e-3:
            print(f'\nTime: {best_time:.3e}s')
        else:
            print(f'\nTime: {best_time:.3f}s')
    
    return best_time

def _flatten(items):
    def iterate(i):
        if isinstance(i, Iterable) and not isinstance(i, str):
            for ii in i:
                yield from _flatten(ii)
        else:
            yield i
    return np.asanyarray( list(iterate(items)) )

def _make_validation_func(thresh:float, output_example):
    if isinstance( output_example, Iterable ) and not isinstance(output_example, str):
        if thresh:
            return lambda a,b: (np.abs(_flatten(a)-_flatten(b)) < thresh).all()
        else:
            def f(a,b):
                a_ = _flatten(a)
                b_ = _flatten(b)
                if len(a_) != len(b_): return False
                return (a_ == b_).all()
            return f
            # return lambda a,b: (_flatten(a) == _flatten(b)).all()
            
    else:
        if thresh:
            return lambda a,b: abs(a-b) < thresh
        else:
            return lambda a,b: a==b
        



def test_all(
    test_cases: List,
    func_list: List[Tuple],
    display:bool = False,
    check_thresh:float=None,
    test_only:bool=False,
    repeat:int=5,
    number:int=1000
) -> None:

    n_func = len(func_list)
    successes = []
    times = []

    validate_func = _make_validation_func(check_thresh, test_cases[0][1])
    nargs = len(inspect.signature(func_list[0]).parameters)
    
    # for i, (inp, out) in tqdm.tqdm(enumerate(test_cases)):
    for i, (inp, out) in enumerate(tqdm.tqdm(test_cases)):
        test_passes = list()
        test_times  = list()

        if display: print(f'\n==== Test Case {i} ==== \n')

        for j, fnc in enumerate(func_list):
            s = check_soln(
                fnc, 
                inp, 
                out, 
                validate_func, 
                display=display,
                nargs=nargs
            )
            test_passes.append(s)
            
            if not test_only:
                t = time_soln(
                    fnc,
                    inp,
                    display = display,
                    nargs = nargs, 
                    repeat = repeat,
                    number = number,
                )
                test_times.append(t)

        successes.append(test_passes)
        times.append(test_times)

    if display: print(f'\n==== End of Tests ==== \n')

    # Tests completed
    # Print out summary
    print('---- Results ----')
    for i, test_line in enumerate(successes):
        print(f'Test {i:d}:', ''.join(['❌✅'[int(s)] for s in test_line]))
    print()

    if test_only: return

    print()
    print('---- Times ----')
    for i, test_line in enumerate(times):
        min_time = min(test_line)

        print(f'Test {i:d}', end = '  ')
        for t in test_line:
            if n_func == 1:
                print(f'{t:.6f}')
            elif t == min_time:
                print(f'{"🏆":^5s}', end = '  ')
            else:
                print(f'{t/min_time:5.2f}', end = '  ')
        
        if n_func > 1:
            best_func = func_list[ test_line.index(min_time) ]
            print(best_func.__name__)
    

import argparse
import os
from concurrent.futures import ThreadPoolExecutor
from math import factorial
from random import randint

from decos import timeit

TIMES = None
MAX_WORKERS = None


def __miltiply_range(rng):
    res = 1
    for i in rng:
        res *= i
    return res


@timeit(supress_output=True)
def factorial_multi(n: int):
    tpe = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    part_size = n // MAX_WORKERS

    ranges = [range(i * part_size, (i + 1) * part_size) for i in range(MAX_WORKERS)]
    results = tpe.map(__miltiply_range, ranges)
    return __miltiply_range(results)


@timeit(supress_output=True)
def factorial_single(n: int):
    return factorial(n)  # встроенная функция в модуле math


def main():
    # selected_number = randint(100000, 500000)
    selected_number = 10 ** 6
    print(f'Selected number for factorial: {selected_number}')

    factorial_multi(selected_number)
    factorial_single(selected_number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ThreadPoolExecutor')
    parser.add_argument('--workers', metavar='WORKERS', type=int,
                        help='set number of workers for ThreadPoolExecutor')
    parser.add_argument('--times', metavar='TIMES', type=int,
                        help='run N tests times')

    args = parser.parse_args()

    MAX_WORKERS = args.workers or os.cpu_count()
    TIMES = args.times or randint(1, 10)

    print('-' * 10, 'Start Test!', '-' * 10)
    print(f'[*] Workers: {MAX_WORKERS}')
    print(f'[*] Times: {TIMES}', '\n')
    main()
    print('-' * 10, 'End Test!', '-' * 10)
import math

from decos import timeit


@timeit()
def math_factorial(n):
    return math.factorial(n)


def main():
    """Основная функция запускающая тесты."""
    # selected_number = randint(100000, 500000)
    selected_number = 2 * 10 ** 5
    print(f'Selected number for factorial: {selected_number}')

    math_factorial(selected_number)


if __name__ == "__main__":
    print('-' * 10, 'Start Test!', '-' * 10)
    main()
    print('-' * 10, 'End Test!', '-' * 10)

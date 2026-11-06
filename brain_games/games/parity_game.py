import random


def get_result_parity():
    number = random.randint(1, 100)
    result = 'yes' if number % 2 == 0 else 'no'

    return number, result
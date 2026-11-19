import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def get_gcd(first, second):
    while second:
        first, second = second, first % second
    return first


def get_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    print(f'Question: {first_number} {second_number}')
    result = get_gcd(first_number, second_number)

    return str(result)
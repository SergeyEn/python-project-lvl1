import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_round():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    result = 'yes' if number % 2 == 0 else 'no'

    return result
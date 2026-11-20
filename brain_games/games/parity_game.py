import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_round():
    number = random.randint(1, 100)
    question = f'{number}'
    result = 'yes' if number % 2 == 0 else 'no'

    return question, result
import random
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def get_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_round():
    random_number = random.randint(1, 105)
    print(f'Question: {random_number}')
    result = 'yes' if get_prime(random_number) else 'no'

    return result
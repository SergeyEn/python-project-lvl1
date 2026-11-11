import random
import math


def get_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_result_prime():
    random_number = random.randint(1, 105)
    question = f'{random_number}'
    result = 'yes' if get_prime(random_number) else 'no'

    return question, result
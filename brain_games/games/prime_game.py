import random


def get_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_result_prime():
    random_number = random.randint(1, 105)
    question = f'{random_number}'
    result = 'yes' if get_prime(random_number) else 'no'

    return question, result
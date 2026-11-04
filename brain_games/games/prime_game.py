from brain_games.engine import engine
import random
import prompt


def get_prime(n):
    if n < 2:
        return 'no'
    elif n == 2:
        return 'no'
    
    for i in range(2, n):
        if n % i == 0:
            return 'no'
    return 'yes'


def prime_game():
    def get_result():
        random_number = random.randint(1, 105)
        question = f'{random_number}'
        result = get_prime(random_number)

        return question, result

    answer = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    engine(answer, prompt.string, get_result)
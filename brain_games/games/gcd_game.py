from brain_games.engine import engine
import random
import prompt


def get_gcd(first, second):
    while second:
        first, second = second, first % second
    return first


def gcd_game():
    def get_result():
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        question = f'{first_number} {second_number}'
        result = get_gcd(first_number, second_number)

        return question, result

    answer = 'Find the greatest common divisor of given numbers.'

    engine(answer, prompt.integer, get_result)
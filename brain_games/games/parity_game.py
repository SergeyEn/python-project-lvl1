from brain_games.engine import engine
import random
import prompt


def parity_game():
    def get_result():
        number = random.randint(1, 100)
        result = 'yes' if number % 2 == 0 else 'no'

        return number, result

    answer = 'Answer "yes" if the number is even, otherwise answer "no".'

    engine(answer, prompt.string, get_result)
from brain_games.engine import engine
import random
import prompt


def make_list():
    sum_element = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 5)
    result_list = [start + i * step for i in range(sum_element)]
    return result_list


def progression_game():
    def get_result():
        get_list = make_list()
        random_index = random.randint(0, len(get_list) - 1)
        result = get_list[random_index]
        get_list[random_index] = ".."
        question = f'{" ".join(str(i) for i in get_list)}'
        
        return question, result

    answer = 'What number is missing in the progression?'

    engine(answer, prompt.integer, get_result)
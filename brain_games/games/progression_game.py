import random


def make_list():
    sum_element = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 5)
    result_list = [start + i * step for i in range(sum_element)]
    return result_list


def get_result_progression():
    get_list = make_list()
    random_index = random.randint(0, len(get_list) - 1)
    result = get_list[random_index]
    get_list[random_index] = ".."
    question = f'{" ".join(str(i) for i in get_list)}'
        
    return question, result
from general_logics import welcome_prompt, victory
from general_logics import get_answer
from random import randint

def get_progression(start_num, long_list):
    list = []
    for count_pro in range(long_list):
        list.append(start_num)
        start_num += 2
    return list

def log_progression():
    name  = welcome_prompt()
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        random_start = randint(1, 50)
        long_progression = randint(5, 11)
        count_list = get_progression(random_start, long_progression)
        rnd_index = randint(1, len(count_list) - 1)
        result = count_list[rnd_index]
        count_list[rnd_index] = '..'
        new_list = str(count_list).replace("'", '')
        print(f"Question: {str(new_list).replace(',', '')[1:-1]}")
        answer = int(input('Your answer: '))
        get_answ = get_answer(answer, result, name)
        if get_answ == False:
            break
        count += 1
    victory(count, name)

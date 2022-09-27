from brain_games.games.general_logics import welcome_prompt, random_num
from brain_games.games.general_logics import victory, get_answer

def get_even_num(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def parity_check():
    user_name = welcome_prompt()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        random_number = random_num()
        print(random_number)
        answer = input('Question: ')
        get_answ = get_answer(answer, get_even_num(random_number), user_name)
        if get_answ == False:
            break
        count += 1
    victory(count, user_name)

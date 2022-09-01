from general_logics import victory, get_answer
from general_logics import welcome_prompt, random_num
from random import choice


def get_calc(num1, num2, random_operation):
    operation = '+-*'
    if random_operation == '+':
        return num1 + num2
    elif random_operation == '-':
        return num1 - num2
    else:
        return num1 * num2

def calc_logic():
    name = welcome_prompt()
    print("What is the result of the expression?")
    count = 0
    oper = '+-*'

    while count < 3:
        random_num1 = random_num()
        random_num2 = random_num()
        random_oper = choice(oper)
        print(f'Question: {random_num1} {random_oper} {random_num2}')
        answer = int(input('Your answer: '))
        result = get_calc(random_num1, random_num2, random_oper)
        get_answ = get_answer(answer, result, name)
        if get_answ == False:
            break
        count += 1
    victory(count, name)

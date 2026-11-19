import random


DESCRIPTION = 'What is the result of the expression?'

def get_calc(first_num, second_num, oper):
    if oper == '+':
        return first_num + second_num
    elif oper == '*':
        return first_num * second_num
    else:
        return first_num - second_num



def get_round():
    operation_list = random.choice(['+', '-', '*'])
    first_number = random.randint(1, 59)
    second_number = random.randint(1, 59)
    print(f'Question: {first_number} {operation_list} {second_number}')
    result = get_calc(first_number, second_number, operation_list)

    return str(result)
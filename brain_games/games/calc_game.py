from brain_games.engine import engine
import random
import prompt


def get_calc(first_num, second_num, oper):
    if oper == '+':
        return first_num + second_num
    elif oper == '*':
        return first_num * second_num
    else:
        return first_num - second_num


def calc_game():
    def get_result():
        operation_list = random.choice(['+', '-', '*'])
        first_number = random.randint(1, 59)
        second_number = random.randint(1, 59)
        question = f'{first_number} {operation_list} {second_number}'
        result = get_calc(first_number, second_number, operation_list)

        return question, result


    answer = 'What is the result of the expression?'
    engine(answer, prompt.integer, get_result)
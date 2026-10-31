import prompt
import random
from brain_games.games.greet_module import greet


def calc(first_num, second_num, oper):
    if oper == '+':
        return first_num + second_num
    elif oper == '*':
        return first_num * second_num
    else:
        return first_num - second_num


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def parity_game():
    greet()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        random_number = random.randint(1, 50)
        print(f'Question: {random_number}')
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.\nCorrect answer was '{correct_answer}.'")
            break
        count += 1
        if count == 3:
            print(f'Congratulation, {name}!')


def calc_game():
    greet()
    name = welcome_user()
    print('What is the result of the expression?')
    operation_list = ['+', '-', '*']
    count = 0

    while count < 3:
        first_number = random.randint(1, 50)
        second_number = random.randint(1, 50)
        operation = random.choice(operation_list)
        print(f'Question: {first_number} {operation} {second_number}')
        user_answer = prompt.integer('Your answer: ')
        result = calc(first_number, second_number, operation)
        if user_answer == result:
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(.\nCorrect answer was {result}.')
            break
        count += 1
        if count == 3:
            print(f'Congratulation, {name}!')

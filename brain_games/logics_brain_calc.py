from random import choice, randint
import prompt


def calc_logic():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May i have your name? ')
    print(f'Hello, {user_name}')
    print("What is the result of the expression?")
    count = 0
    oper = '+-*'
    result = 0

    for count in range(3):
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 100)
        random_oper = choice(oper)
        print(f'Question: {random_num1} {random_oper} {random_num2}')
        answer = input('Your answer: ')
        if random_oper == '+':
            result = random_num1 + random_num2
            if int(answer) == result:
                print('Correct!')
            else: 
                print(f"{answer} is wrong answer ;(. Correct answer was '{result}'")
                break
        if random_oper == '-':
            result = random_num1 - random_num2
            if int(answer) == result:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was '{result}'")
                break
        if random_oper == '*':
            result = random_num1 * random_num2
            if int(answer) == result:
                print('Correct!')
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was '{result}'")
                break
        print(count)


calc_logic()

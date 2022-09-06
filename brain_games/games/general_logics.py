from random import randint
import prompt


def welcome_prompt():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def random_num():
    random_number = randint(1, 100)
    return random_number


def victory(count, name):
    if count == 3:
        print(f'Congratulations, {name}!')


def get_answer(answer, question, name):
    if question == answer:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{question}'.")
        print(f"Let's try again, {name}!")
        return False

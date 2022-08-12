import prompt
from random import randint


def search_gcd():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    gcd_result = 0

    while count < 3:
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 100)
        print(f'Question: {random_num1} {random_num2}')
        answer = input('Your answer: ')
        while random_num1 != 0 and random_num2 != 0:
            if random_num1 > random_num2:
                random_num1 = random_num1 % random_num2
            else:
                random_num2 = random_num2 % random_num1
        if random_num1 != 0:
            gcd_result = random_num1
        else:
            gcd_result = random_num2
        if gcd_result == int(answer):
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {gcd_result}.')
            print(f"Let's try again, {user_name}")
            break

        count += 1
    if count == 3:
        print(f'Congratulations, {user_name}!')

import prompt
from random import randint


def parity_check():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count < 3:
        random_number = randint(1, 100)
        print(random_number)
        answer = input('Question: ')
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif random_number % 2 != 0 and answer == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {user_name}!")
            break

        count += 1
    if count == 3:
        print(f'Congratulations, {user_name}!')


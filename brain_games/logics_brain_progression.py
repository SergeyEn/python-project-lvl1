import prompt
from random import randint


def log_progression():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    count = 0
    count_list = []
    while count < 3:
        count_list.clear()
        random_start = randint(1, 50)
        long_progression = randint(5, 11)
        for count_pro in range(long_progression):
            count_list.append(random_start)
            random_start += 2
        rnd_index = randint(1, len(count_list) - 1)
        result = count_list[rnd_index]
        count_list[rnd_index] = '..'
        new_list = str(count_list).replace("'", '')
        print(f"Question: {str(new_list).replace(',', '')[1:-1]}")
        answer = input('Your answer: ')
        if int(answer) == result:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
            print(f"Let's try again, {user_name}")
            break

        count += 1

    if count == 3:
        print(f'Congratulations, {user_name}!')

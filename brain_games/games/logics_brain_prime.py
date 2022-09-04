from itertools import count
from general_logics import welcome_prompt, victory
from random import randint

def get_count_prime(num):
    count_prime = 0
    for i in range(2, num):
        if(num % i == 0):
            count_prime += 1
    return count_prime

def log_prime():
    name = welcome_prompt()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    count = 0

    while count < 3:
        count_prime = 0
        random_num = randint(2, 100)
        print(f"Question: {random_num}")
        get_count_prime(random_num)
        answer = input("Your answer: ")
        if count_prime == 0 and answer == "yes":
            print('Correct!')
        elif count_prime != 0 and answer == "no":
            print('Correct!')
        else:
            if answer == 'yes':
                right_result = 'no'
            else:
                right_result = 'yes'
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_result}'.")
            print(f"Let's try again, {user_name}")
            break
        count += 1
    victory(count, name)


log_prime()

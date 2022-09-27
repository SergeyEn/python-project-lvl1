from brain_games.games.general_logics import welcome_prompt, victory, get_answer
from random import randint


def get_count_prime(num):
    count_prime = 0
    for i in range(2, num):
        if(num % i == 0):
            count_prime += 1
    return count_prime


def get_result(num_prime):
    if num_prime == 0:
        return 'yes'
    else:
        return 'no'


def log_prime():
    name = welcome_prompt()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    count = 0

    while count < 3:
        random_num = randint(2, 100)
        print(f"Question: {random_num}")
        count_prime = get_count_prime(random_num)
        answer = input("Your answer: ")
        result = get_result(count_prime)
        get_answ = get_answer(answer, result, name)
        if get_answ == False:
            break
        count += 1
    victory(count, name)

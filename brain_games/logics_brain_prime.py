import prompt
from random import randint


def log_prime():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    count = 0    

    while count < 3:
        count_prime = 0
        random_num = randint(2,100)
        print(f"Question: {random_num}")
        for i in range(2, random_num ):
            if (random_num % i == 0):
                count_prime += 1
        answer = input("Your answer: ")
        if count_prime == 0 and answer == "yes":
            print('Correct!')
        elif count_prime != 0 and answer == "no":
            print('Correct!')
        else:
            if answer == 'yes': right_result = 'no' 
            else:   right_result = 'yes' 
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_result}'.")
            print(f"Let's try again, {user_name}")
            break

        count += 1

    if count == 3:
            print(f'Congratulations, {user_name}!')




    
         


log_prime()
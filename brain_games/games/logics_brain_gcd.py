from general_logics import welcome_prompt, random_num
from general_logics import get_answer, victory


def get_gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

def search_gcd():
    name = welcome_prompt()
    print('Find the greatest common divisor of given numbers.')
    count = 0

    while count < 3:
        random_num1 = random_num()
        random_num2 = random_num()
        print(f'Question: {random_num1} {random_num2}')
        answer = int(input('Your answer: '))
        gcd_result = get_gcd(random_num1, random_num2)
        get_answ = get_answer(answer, gcd_result, name)
        if get_answ == False:
            break
        count += 1
    victory(count, name)

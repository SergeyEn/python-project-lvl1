import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine(question, get_answer, get_result):
    name = welcome_user()
    print(question)

    count = 0

    while count < 3:
        question_text, result = get_result()

        print(f'Question: {question_text}')
        user_answer = get_answer('Your answer: ')

        if user_answer == result:
            print('Correct!')
        else:
            print(
                f'{user_answer} is wrong answer ;(.\n'
                f'Correct answer was {result}.'
            )
            break

        count += 1

    if count == 3:
        print(f'Congratulation, {name}!')
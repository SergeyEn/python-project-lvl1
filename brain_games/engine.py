from brain_games.cli import welcome_user


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
                f'Correct answer was {result}.\n'
                f"Let's try again, {name}!"
            )
            break

        count += 1

    if count == 3:
        print(f'Congratulations, {name}!')
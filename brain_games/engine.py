from brain_games.cli import welcome_user
import prompt


def engine(game):
    name = welcome_user()
    print(game.DESCRIPTION)

    count = 0

    while count < 3:
        question, result = game.get_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == result:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(.\nCorrect answer was {result}.\nLet's try again, {name}!")
            break

        count += 1

    if count == 3:
        print(f'Congratulations, {name}!')
from brain_games.games.parity_game import get_result_parity
from brain_games.engine import engine
import prompt


def main():
    engine('Answer "yes" if the number is even, otherwise answer "no".', prompt.string, get_result_parity)
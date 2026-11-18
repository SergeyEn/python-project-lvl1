from brain_games.games.parity_game import get_result_parity
from brain_games.engine import engine
import prompt


RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'

def main():
    engine(RULES_EVEN, prompt.string, get_result_parity)
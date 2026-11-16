from brain_games.games.parity_game import get_result_parity
from brain_games.engine import engine
from brain_games.rules_games import RULES_EVEN
import prompt


def main():
    engine(RULES_EVEN, prompt.string, get_result_parity)
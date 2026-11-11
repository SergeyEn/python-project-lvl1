from brain_games.games.gcd_game import get_result_gcd
from brain_games.engine import engine
from brain_games.rules_games import RULES_GCD
import prompt


def main():
    engine(RULES_GCD, prompt.integer, get_result_gcd)
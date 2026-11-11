from brain_games.games.calc_game import get_result_calc
from brain_games.engine import engine
from brain_games.rules_games import RULES_CALC
import prompt


def main():
    engine(RULES_CALC, prompt.integer, get_result_calc)
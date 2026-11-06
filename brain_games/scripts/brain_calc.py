from brain_games.games.calc_game import get_result_calc
from brain_games.engine import engine
import prompt


def main():
    engine('What is the result of the expression?', prompt.integer, get_result_calc)
from brain_games.games.calc_game import get_result_calc
from brain_games.engine import engine
import prompt


RULES_CALC = 'What is the result of the expression?'

def main():
    engine(RULES_CALC, prompt.integer, get_result_calc)
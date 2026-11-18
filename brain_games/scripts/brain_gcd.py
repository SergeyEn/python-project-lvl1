from brain_games.games.gcd_game import get_result_gcd
from brain_games.engine import engine
import prompt


RULES_GCD = 'Find the greatest common divisor of given numbers.'

def main():
    engine(RULES_GCD, prompt.integer, get_result_gcd)
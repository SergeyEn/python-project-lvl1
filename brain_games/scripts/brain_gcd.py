from brain_games.games.gcd_game import get_result_gcd
from brain_games.engine import engine
import prompt


def main():
    engine('Find the greatest common divisor of given numbers.', prompt.integer, get_result_gcd)
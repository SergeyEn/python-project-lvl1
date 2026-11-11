from brain_games.games.prime_game import get_result_prime
from brain_games.engine import engine
from brain_games.rules_games import RULES_STRING
import prompt


def main():
    engine(RULES_STRING, prompt.string, get_result_prime)
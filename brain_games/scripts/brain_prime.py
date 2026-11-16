from brain_games.games.prime_game import get_result_prime
from brain_games.engine import engine
from brain_games.rules_games import RULES_PRIME
import prompt


def main():
    engine(RULES_PRIME, prompt.string, get_result_prime)
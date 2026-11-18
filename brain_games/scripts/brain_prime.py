from brain_games.games.prime_game import get_result_prime
from brain_games.engine import engine
import prompt


RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def main():
    engine(RULES_PRIME, prompt.string, get_result_prime)
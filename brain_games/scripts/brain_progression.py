from brain_games.games.progression_game import get_result_progression
from brain_games.engine import engine
import prompt


def main():
    engine('Answer "yes" if given number is prime. Otherwise answer "no".', prompt.string, get_result_progression)
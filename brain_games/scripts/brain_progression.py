from brain_games.games.progression_game import get_result_progression
from brain_games.engine import engine
from brain_games.rules_games import RULES_PROGRESSION
import prompt


def main():
    engine(RULES_PROGRESSION, prompt.integer, get_result_progression)
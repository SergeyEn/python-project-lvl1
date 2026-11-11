from brain_games.games.progression_game import get_result_progression
from brain_games.engine import engine
from brain_games.rules_games import RULES_STRING
import prompt


def main():
    engine(RULES_STRING, prompt.integer, get_result_progression)
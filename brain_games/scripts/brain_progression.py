from brain_games.games.progression_game import get_result_progression
from brain_games.engine import engine
import prompt


RULES_PROGRESSION = 'What number is missing in the progression?'

def main():
    engine(RULES_PROGRESSION, prompt.integer, get_result_progression)
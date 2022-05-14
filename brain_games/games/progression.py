"""The progression game. Find missing number in the progression."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MIN_START = -100
MAX_START = 1000
MAX_STEP = 50


def run_round():
    """Get data for the one round of the brain-progression game.

    Returns:
        case: generated progression with one random item hidden,
        hidden_number: correct answer
    """
    progression = []
    number = randint(MIN_START, MAX_START)
    step = randint(1, MAX_STEP)

    for _ in range(PROGRESSION_LENGTH):
        progression.append(str(number))
        number += step

    index_to_hide = randint(0, PROGRESSION_LENGTH - 1)
    hidden_number = progression[index_to_hide]
    progression[index_to_hide] = '..'

    case = ' '.join(progression)

    return (case, hidden_number)

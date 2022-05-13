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
        case: generated progression,
        hidden_number: correct_answer
    """
    case = ''
    number = randint(MIN_START, MAX_START)
    step = randint(1, MAX_STEP)
    index_to_hide = randint(0, PROGRESSION_LENGTH - 1)
    hidden_number = ''

    i = 0
    while i < PROGRESSION_LENGTH:
        if i == index_to_hide:
            hidden_number += str(number)
            case = '{case} {add}'.format(case=case, add='..')
        else:
            case = '{case} {add}'.format(case=case, add=str(number))

        number += step
        i += 1

    return (case.strip(), hidden_number)

"""The even numbers game. Is generated number even or not."""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = -1000000000
MAX_NUMBER = 1000000000


def _is_even(number):
    return number % 2 == 0


def _get_correct_answer(number):
    if _is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (correct_answer)


def get_game_round():
    """Get data for the one round of the brain-even game.

    Returns:
        case: generated number,
        correct_answer
    """
    case = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = _get_correct_answer(case)

    return (case, correct_answer)

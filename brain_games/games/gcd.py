"""The greatest common divisor game.

Find the greatest common divisor of given numbers.
"""

import math
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 50


def _get_case():
    num_a = randint(MIN_NUMBER, MAX_NUMBER)
    num_b = randint(MIN_NUMBER, MAX_NUMBER)
    case = '{num_a} {num_b}'.format(num_a=num_a, num_b=num_b)

    return (case, num_a, num_b)


def _get_correct_answer(num_a, num_b):
    return str(math.gcd(num_a, num_b))


def get_game_round():
    """Get data for the one round of the brain-gcd game.

    Returns:
        case: generated case of two numbers,
        correct_answer
    """
    (case, num_a, num_b) = _get_case()
    correct_answer = _get_correct_answer(num_a, num_b)

    return (case, correct_answer)

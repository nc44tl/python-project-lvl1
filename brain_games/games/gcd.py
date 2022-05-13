"""The greatest common divisor game.

Find the greatest common divisor of given numbers.
"""

import math
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 50


def run_round():
    """Get data for the one round of the brain-gcd game.

    Returns:
        case: generated case of two numbers,
        correct_answer
    """
    num_a = randint(MIN_NUMBER, MAX_NUMBER)
    num_b = randint(MIN_NUMBER, MAX_NUMBER)
    case = f'{num_a} {num_b}'
    correct_answer = str(math.gcd(num_a, num_b))

    return (case, correct_answer)

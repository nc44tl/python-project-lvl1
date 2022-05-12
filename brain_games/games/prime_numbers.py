"""The prime_numbers_game. Is generated number prime or not."""

from math import sqrt
from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 500


def _is_prime(number):
    if number % 2 == 0:
        return number == 2
    for i in range(3, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def get_game_round():
    """Get data for the one round of the brain-prime game.

    Returns:
        number: generated number,
        correct_answer
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if _is_prime(number) else 'no'

    return (number, correct_answer)

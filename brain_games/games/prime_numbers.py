"""The prime_numbers_game. Is generated number prime or not."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 500


def _is_prime(number):
    if number % 2 == 0:
        return number == 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number


def _get_correct_answer(number):
    if _is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (correct_answer)


def get_game_round():
    """Get data for the one round of the brain-prime game.

    Returns:
        case: generated number,
        correct_answer
    """
    case = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = _get_correct_answer(case)

    return (case, correct_answer)

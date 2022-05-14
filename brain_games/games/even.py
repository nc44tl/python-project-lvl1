"""The even numbers game. Is generated number even or not."""

from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = -1000000000
MAX_NUMBER = 1000000000


def run_round():
    """Get data for the one round of the brain-even game.

    Returns:
        number: generated number,
        correct_answer
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    return (number, correct_answer)

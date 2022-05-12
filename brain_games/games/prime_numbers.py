"""The prime_numbers_game. Is generated number prime or not."""

from random import randint

import prompt
from brain_games.cli import ANSWER_PROMPT, QUESTION_STRING
from brain_games.game import check_user_answer

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


def game_round():
    """One round of brain-prime game.

    Returns:
        res: result of the round (boolean),
        user_unswer,
        correct_answer
    """
    case = randint(MIN_NUMBER, MAX_NUMBER)

    print(QUESTION_STRING + str(case))
    user_answer = prompt.string(ANSWER_PROMPT)

    correct_answer = _get_correct_answer(case)
    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

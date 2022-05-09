"""The calculation game. User solves generated cases."""

import math

import prompt
from brain_games.cli import ANSWER_PROMPT, QUESTION_STRING
from brain_games.games.game import check_user_answer, get_number

_MIN_NUMBER = 1
_MAX_NUMBER = 50


def _get_case():
    num_a = get_number(_MIN_NUMBER, _MAX_NUMBER)
    num_b = get_number(_MIN_NUMBER, _MAX_NUMBER)
    case = '{num_a} {num_b}'.format(num_a=num_a, num_b=num_b)

    return (case, num_a, num_b)


def _get_correct_answer(num_a, num_b):
    return str(math.gcd(num_a, num_b))


def gcd_game():  # noqa: WPS210 too many local variables
    """One round of brain-gcd game.

    Returns:
        res = result of the round (boolean),
        user_unswer,
        correct_answer
    """
    (case, num_a, num_b) = _get_case()

    print(QUESTION_STRING + case)
    correct_answer = _get_correct_answer(num_a, num_b)
    user_answer = prompt.string(ANSWER_PROMPT)

    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

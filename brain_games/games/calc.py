"""The calculation game. User solves generated cases."""

from random import randint

import prompt
from brain_games.cli import ANSWER_PROMPT, QUESTION_STRING
from brain_games.game import check_user_answer, get_number


def _get_operator():
    operators = ('+', '-', '*')
    ind = randint(0, 2)
    return operators[ind]


_MIN_NUMBER = -10
_MAX_NUMBER = 10


def _get_case():
    a = get_number(_MIN_NUMBER, _MAX_NUMBER)
    b = get_number(_MIN_NUMBER, _MAX_NUMBER)
    operator = _get_operator()

    return '{a} {operator} {b}'.format(a=a, operator=operator, b=b)


def _get_correct_answer(case):
    return str(eval(case))  # noqa: S307 Use of possibly insecure function


def calc_game():
    """One round of brain-calc game.

    Returns:
        res = result of the round (True or False),
        user_unswer,
        correct_answer
    """
    case = _get_case()

    print(QUESTION_STRING + case)
    correct_answer = _get_correct_answer(case)
    user_answer = prompt.string(ANSWER_PROMPT)

    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

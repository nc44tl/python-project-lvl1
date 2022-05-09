"""The calculation game. User solves generated cases."""

from random import randint

import prompt
from brain_games.cli import answer_prompt, question_string
from brain_games.game import check_user_answer, get_number


def _get_operator():
    operators = ('+', '-', '*')
    ind = randint(0, 2)
    return operators[ind]


min_number = -10
max_number = 10


def _get_case():
    a = get_number(min_number, max_number)
    b = get_number(min_number, max_number)
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

    print(question_string + case)
    correct_answer = _get_correct_answer(case)
    user_answer = prompt.string(answer_prompt)

    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

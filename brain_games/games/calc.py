"""The calculation game. User solves generated cases."""

from random import randint

from brain_games.game import (
    get_number,
    check_user_answer,
)
from brain_games.cli import (
    question_string,
    answer_prompt,
)

import prompt


def _get_operator():
    operators = ('+', '-', '*')
    ind = randint(0, 2)
    return operators[ind]


"""Difficulty adjustment."""
min_number = -10
max_number = 10


def _get_case():
    a = get_number(min_number, max_number)
    b = get_number(min_number, max_number)
    op = _get_operator()

    return '{a} {op} {b}'.format(a=a, op=op, b=b)


def _get_correct_answer(case):
    return str(eval(case))


def calc_game():
    case = _get_case()

    print(question_string + case)
    user_answer = prompt.string(answer_prompt)

    correct_answer = _get_correct_answer(case)
    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)


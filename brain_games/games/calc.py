"""The calculation game. User solves generated cases."""

from random import randint

from brain_games.game import (
    get_number,
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


min = -10
max = 10


def get_case():
    a = get_number(min, max)
    b = get_number(min, max)
    op = _get_operator()

    return f'{a} {op} {b}'


def get_correct_answer(case):
    return str(eval(case))


def check_user_answer(user_answer, correct_answer):
    return user_answer == correct_answer


def calc_game():
    case = get_case()

    print(question_string + case)
    user_answer = prompt.string(answer_prompt)

    correct_answer = get_correct_answer(case)
    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)


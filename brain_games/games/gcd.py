"""The calculation game. User solves generated cases."""

import math

import prompt
from brain_games.cli import answer_prompt, question_string
from brain_games.game import check_user_answer, get_number

min_number = 1
max_number = 50


def _get_case():
    num_a = get_number(min_number, max_number)
    num_b = get_number(min_number, max_number)
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

    print(question_string + case)
    correct_answer = _get_correct_answer(num_a, num_b)
    user_answer = prompt.string(answer_prompt)

    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

"""The calculation game. User solves generated cases."""

import prompt
from brain_games.cli import answer_prompt, question_string
from brain_games.game import check_user_answer, get_number

min_number = 1
max_number = 10


def _get_case():
    a = get_number(min_number, max_number)  # noqa: WPS111 too short name
    b = get_number(min_number, max_number)  # noqa: WPS111 too short name

    return '{a} {b}'.format(a=a, b=b)


def _get_correct_answer(case):
    return case


def gcd_game():
    """One round of brain-gcd game.

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

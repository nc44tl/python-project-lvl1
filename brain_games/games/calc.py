"""The calculation game. Find the result of the generated expression."""

from random import randint

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = -10
MAX_NUMBER = 10


def _get_operator():
    operators = ('+', '-', '*')
    ind = randint(0, 2)
    return operators[ind]


def _get_case():
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    operator = _get_operator()

    return '{a} {operator} {b}'.format(a=a, operator=operator, b=b)


def _get_correct_answer(case):
    return str(eval(case))  # noqa: S307 Use of possibly insecure function


def get_game_round():
    """Get data for the one round of the brain-calc game.

    Returns:
        case: generated expression,
        correct_answer
    """
    case = _get_case()
    correct_answer = _get_correct_answer(case)

    return (case, correct_answer)

"""The even numbers game. Is generated number even or not."""

from random import randint

import prompt
from brain_games.cli import ANSWER_PROMPT, QUESTION_STRING
from brain_games.game import check_user_answer

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = -1000000000
MAX_NUMBER = 1000000000


def _is_even(number):
    return number % 2 == 0


def _get_correct_answer(number):
    if _is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (correct_answer)


def game_round():
    """One round of brain-even game.

    Returns:
        res = result of the round (boolean),
        user_unswer,
        correct_answer
    """
    case = randint(MIN_NUMBER, MAX_NUMBER)

    print(QUESTION_STRING + str(case))
    user_answer = prompt.string(ANSWER_PROMPT)

    correct_answer = _get_correct_answer(case)
    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

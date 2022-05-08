"""The even_numbers_game. User answers, if generated number is even or not."""

from brain_games.game import get_number
from brain_games.cli import (
    question_string,
    answer_prompt_string,
)

import prompt


def _is_even(number):
    return number % 2 == 0


def _check_answer(number, answer):
    if _is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (answer == correct_answer, correct_answer)


def even_numbers_game():
    number = get_number()

    print(question_string + str(number))
    answer = prompt.string(answer_prompt_string)
    (res, correct_answer) = _check_answer(number, answer)

    return (res, answer, correct_answer)

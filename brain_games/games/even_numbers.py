"""The even_numbers_game. User answers, if generated number is even or not."""

from brain_games.game import (
    get_number,
    check_user_answer,
)
from brain_games.cli import (
    question_string,
    answer_prompt,
)

import prompt


def _is_even(number):
    return number % 2 == 0


def _get_correct_answer(number):
    if _is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (correct_answer)


min_number = -1000000000
max_number = 1000000000


def even_numbers_game():
    case = get_number(min_number, max_number)

    print(question_string + str(case))
    user_answer = prompt.string(answer_prompt)
    
    correct_answer = _get_correct_answer(case)
    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

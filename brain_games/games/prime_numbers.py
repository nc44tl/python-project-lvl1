"""The even_numbers_game. User answers, if generated number is even or not."""

import prompt
from brain_games.cli import answer_prompt, question_string
from brain_games.game import check_user_answer, get_number


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


def prime_numbers_game():
    """One round of brain-even game.

    Returns:
        res = result of the round (boolean),
        user_unswer,
        correct_answer
    """
    case = get_number(min_number, max_number)

    print(question_string + str(case))
    user_answer = prompt.string(answer_prompt)

    correct_answer = _get_correct_answer(case)
    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

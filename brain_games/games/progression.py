"""The progression game. Find missing number in the progression."""

import prompt
from brain_games.cli import ANSWER_PROMPT, QUESTION_STRING
from brain_games.game import check_user_answer, get_number

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MIN_START = -100
MAX_START = 1000
MAX_STEP = 50


def _get_progression():
    case = ''
    number = get_number(MIN_START, MAX_START)
    step = get_number(1, MAX_STEP)
    index_to_hide = get_number(0, PROGRESSION_LENGTH - 1)
    hidden_number = ''

    i = 0
    while i < PROGRESSION_LENGTH:
        if i == index_to_hide:
            hidden_number += str(number)
            case = '{case} {add}'.format(case=case, add='..')
        else:
            case = '{case} {add}'.format(case=case, add=str(number))

        number += step
        i += 1

    return (case.strip(), hidden_number)


def game_round():
    """One round of the brain-progression game.

    Returns:
        res: result of the round (boolean),
        correct_answer
        user_unswer,
    """
    (case, correct_answer) = _get_progression()

    print(QUESTION_STRING + case)
    user_answer = prompt.string(ANSWER_PROMPT)

    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

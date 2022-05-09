"""The progression game. Needed to find missing number in the progression."""

import prompt
from brain_games.cli import answer_prompt, question_string
from brain_games.game import check_user_answer, get_number

progression_length = 10
min_start = -100
max_start = 1000
max_step = 50


def _get_progression():
    case = ''
    number = get_number(min_start, max_start)
    step = get_number(1, max_step)
    index_to_hide = get_number(0, progression_length - 1)
    hidden_number = ''

    i = 0
    while i < progression_length:
        if i == index_to_hide:
            hidden_number += str(number)
            case = '{case} {add}'.format(case=case, add='..')
        else:
            case = '{case} {add}'.format(case=case, add=str(number))

        number += step
        i += 1

    return (case, hidden_number)


def progression_game():
    """One round of brain-progression game.

    Returns:
        res: result of the round (boolean),
        correct_answer
        user_unswer,
    """
    (case, correct_answer) = _get_progression()

    print(question_string + case)
    user_answer = prompt.string(answer_prompt)

    res = check_user_answer(user_answer, correct_answer)

    return (res, user_answer, correct_answer)

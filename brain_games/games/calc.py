"""The calculation game. User solves generated cases."""

import sys
from random import randint

import prompt


def _get_number():
    return randint(-sys.maxsize, sys.maxsize)


def _is_even(number):
    return number % 2 == 0


def _check_answer(number, answer):
    if _is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (answer == correct_answer, correct_answer)


game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def calc_game(user):
    """Gameplay for even_numbers_game.

    Args:
        user: user's name.
    """
    print(game_description)

    counter = 0

    while counter < 3:
        number = _get_number()

        print('Question: {0}'.format(number))
        answer = prompt.string('Your answer: ')

        (res, correct_answer) = _check_answer(number, answer)

        if res:
            print('Correct!')
            counter += 1
        else:
            print(
                "'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {user}!".
                format(
                    answer=answer, correct_answer=correct_answer, user=user,
                ),
            )
            return

    print('Congratulations, {0}!'.format(user))

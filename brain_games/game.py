"""General game algorythm."""


from random import randint

import prompt

ROUNDS_PER_GAME = 3


def get_number(min_number, max_number):
    """Generate random number in range.

    Parameters:
        min_number: range minimum
        max_number: range maximum

    Returns:
        random number from defined range
    """
    return randint(min_number, max_number)


def check_user_answer(user_answer, correct_answer):
    """Compare user_answer with correct_answer.

    Parameters:
        user_answer: user's answer
        correct_answer: correct answer

    Returns:
        boolean
    """
    return user_answer == correct_answer


def run_game(game):
    """General game temlplate.

    Parameters:
        game: module with game
    """
    print('Welcome to the Brain Games!')
    # #TODO после проверки, возможно, убрать ниже дублирование с welcome_user()
    # (dev: 4052e4c). Либо убрать скрипт brain_games и что с ним связано.
    username = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(username))

    print(game.DESCRIPTION)

    counter = 0

    while counter < ROUNDS_PER_GAME:
        (res, user_answer, correct_answer) = game.game_round()
        if not res:
            print("'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {user}!".
                format(  # noqa: E128 (intendation)
                    user_answer=user_answer,
                    correct_answer=correct_answer,
                    user=username,
                ),
            )
            return
        counter += 1

    print('Congratulations, {0}!'.format(username))

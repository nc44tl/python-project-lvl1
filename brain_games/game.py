"""General game algorythm."""


from random import randint

from brain_games.cli import (
    greet,
    print_loose_phrase,
    print_win_phrase,
    welcome_user,
)

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
    greet()
    username = welcome_user()

    print(game.DESCRIPTION)

    counter = 0

    while counter < ROUNDS_PER_GAME:
        (res, user_answer, correct_answer) = game.game_round()
        if not res:
            print_loose_phrase(user_answer, correct_answer, username)
            return
        counter += 1

    print_win_phrase(username)

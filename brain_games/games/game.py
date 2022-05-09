"""General game algorythm."""


from random import randint

from brain_games.cli import (
    print_game_description,
    print_loose_phrase,
    print_win_phrase,
)


def get_number(min_number, max_number):
    """Generate random number in range.

    Parameters:
        min_number: lower border of the range
        max_number: higher border of the range

    Returns:
        random number
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


from brain_games.games.calc import \
    calc_game  # noqa: E402 – at top of file it causes error
from brain_games.games.even_numbers import \
    even_numbers_game  # noqa: E402 – at top of file it causes error
from brain_games.games.gcd import \
    gcd_game  # noqa: E402 – at top of file it causes error
from brain_games.games.prime_numbers import \
    prime_numbers_game  # noqa: E402 – at top of file it causes error
from brain_games.games.progression import \
    progression_game  # noqa: E402 – at top of file it causes error


def _run_round(game):
    if game == 'brain-even':
        (res, user_answer, correct_answer) = even_numbers_game()
    if game == 'brain-calc':
        (res, user_answer, correct_answer) = calc_game()
    if game == 'brain-gcd':
        (res, user_answer, correct_answer) = gcd_game()
    if game == 'brain-progression':
        (res, user_answer, correct_answer) = progression_game()
    if game == 'brain-prime':
        (res, user_answer, correct_answer) = prime_numbers_game()
    return (res, user_answer, correct_answer)


_ROUNDS_PER_GAME = 3


def game(username, game_type):
    """General game temlplate.

    Parameters:
        username: user's name
        game_type: name of the game
    """
    print_game_description(game_type)

    counter = 0

    while counter < _ROUNDS_PER_GAME:
        (res, user_answer, correct_answer) = _run_round(game_type)
        if not res:
            print_loose_phrase(user_answer, correct_answer, username)
            return
        counter += 1

    print_win_phrase(username)

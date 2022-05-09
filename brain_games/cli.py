"""CLI interactions with user."""

import prompt


def greet():
    """Greeting on startup event."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """User acquaintance.

    Returns:
        user's name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


BRAIN_EVEN_DESCRIPTION = 'Answer "yes" if the number is even, \
otherwise answer "no".'
BRAIN_CALC_DESCRIPTION = 'What is the result of the expression?'
BRAIN_GCD_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
BRAIN_PROGRESSION_DESCRIPTION = 'What number is missing in the progression?'
BRAIN_PRIME_DESCRIPTION = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def print_game_description(game):
    """Print game explanation.

    Parameters:
        game: name of the game
    """
    if game == 'brain-even':
        print(BRAIN_EVEN_DESCRIPTION)
        return
    if game == 'brain-calc':
        print(BRAIN_CALC_DESCRIPTION)
        return
    if game == 'brain-gcd':
        print(BRAIN_GCD_DESCRIPTION)
        return
    if game == 'brain-progression':
        print(BRAIN_PROGRESSION_DESCRIPTION)
        return
    if game == 'brain-prime':
        print(BRAIN_PRIME_DESCRIPTION)
        return


QUESTION_STRING = 'Question: '
ANSWER_PROMPT = 'Your answer: '


def print_win_phrase(username):
    """Print win phrase.

    Parameters:
        username: user's name
    """
    print('Congratulations, {0}!'.format(username))


def print_loose_phrase(user_answer, correct_answer, username):
    """Print loose phrase.

    Parameters:
        user_answer: user's answer
        correct_answer: correct answer
        username: user's name
    """
    print("'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {user}!".
        format(  # noqa: E128 (intendation)
            user_answer=user_answer,
            correct_answer=correct_answer,
            user=username,
        ),
    )

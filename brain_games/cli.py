"""CLI interactions."""

import prompt

QUESTION_STRING = 'Question: '
ANSWER_PROMPT = 'Your answer: '


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

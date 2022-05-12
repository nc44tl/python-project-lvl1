"""CLI interactions."""

import prompt

QUESTION_STRING = 'Question: '
ANSWER_PROMPT = 'Your answer: '


def welcome_user():
    """User acquaintance by name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

"""CLI interactions."""

import prompt

QUESTION_STRING = 'Question: '
ANSWER_PROMPT = 'Your answer: '
# Эти константы используются в модуле каждой игры: 5 раз.


def welcome_user():
    """User acquaintance by name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

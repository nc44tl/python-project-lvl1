"""Logic for CLI interactions with user."""

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

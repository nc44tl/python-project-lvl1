"""CLI interactions."""

import prompt


def welcome_user():
    """User acquaintance by name."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

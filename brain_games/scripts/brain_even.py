#!/usr/bin/env python

"""The entry point for brain-even game (is random number even)."""


from brain_games.cli import welcome_user
from brain_games.even_numbers import even_numbers
from brain_games.scripts.brain_games import greet


def main():
    """Run a game."""
    greet()
    welcome_user()
    even_numbers()


if __name__ == '__main__':
    main()

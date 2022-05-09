#!/usr/bin/env python

"""
The entry point for brain-prime game.

Is given number prime or not.
"""


from brain_games.cli import greet, welcome_user
from brain_games.games.game import game


def main():
    """Run a game."""
    greet()
    username = welcome_user()
    game(username, 'brain-prime')


if __name__ == '__main__':
    main()

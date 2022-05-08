#!/usr/bin/env python

"""The entry point for brain-calc game (solve random cases)."""


from brain_games.cli import greet, welcome_user
from brain_games.game import game


def main():
    """Run a game."""
    greet()
    username = welcome_user()
    game(username, 'brain-calc')


if __name__ == '__main__':
    main()

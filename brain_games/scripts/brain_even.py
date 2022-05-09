#!/usr/bin/env python

"""The entry point for brain-even game (is random number even)."""


from brain_games.cli import greet, welcome_user
from brain_games.games.game import game


def main():
    """Run a game."""
    greet()
    username = welcome_user()
    game(username, 'brain-even')


if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""The entry point for brain-calc game (solve random cases)."""


from brain_games.cli import greet
from brain_games.cli import welcome_user
from brain_games.games.calc import calc_game


def main():
    """Run a game."""
    greet()
    name = welcome_user()
    calc_game(name)


if __name__ == '__main__':
    main()

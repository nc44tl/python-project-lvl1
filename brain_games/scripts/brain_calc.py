#!/usr/bin/env python

"""The entry point for brain-even game (is random number even)."""


from brain_games.cli import welcome_user
from brain_games.games.calc import calc_game
from brain_games.scripts.brain_games import greet


def main():
    """Run a game."""
    greet()
    name = welcome_user()
    calc_game(name)


if __name__ == '__main__':
    main()

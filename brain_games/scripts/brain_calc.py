#!/usr/bin/env python

"""The entry point for brain-calc game.

Find the result of random expressions.
"""


from brain_games.game import run_game
from brain_games.games import calc


def main():
    """Run a game."""
    run_game(calc)


if __name__ == '__main__':
    main()

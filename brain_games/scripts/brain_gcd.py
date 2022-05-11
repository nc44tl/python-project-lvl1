#!/usr/bin/env python

"""
The entry point for brain-gcd game.

Find the greatest common divisor of given numbers.
"""


from brain_games.game import run_game
from brain_games.games import gcd


def main():
    """Run a game."""
    run_game(gcd)


if __name__ == '__main__':
    main()

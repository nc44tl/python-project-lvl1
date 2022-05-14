#!/usr/bin/env python

"""
The entry point for brain-prime game.

Is given number prime or not.
"""


from brain_games.game import run_game
from brain_games.games import prime


def main():
    """Run a game."""
    run_game(prime)


if __name__ == '__main__':
    main()

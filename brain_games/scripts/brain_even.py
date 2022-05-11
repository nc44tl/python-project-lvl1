#!/usr/bin/env python

"""The entry point for brain-even game.

Is random number even or not.
"""


from brain_games.game import run_game
from brain_games.games import even_numbers


def main():
    """Run a game."""
    run_game(even_numbers)


if __name__ == '__main__':
    main()

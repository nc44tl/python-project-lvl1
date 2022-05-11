#!/usr/bin/env python

"""The entry point for brain-progression game.

Find missing number in the progression.
"""


from brain_games.game import run_game
from brain_games.games import progression


def main():
    """Run a game."""
    run_game(progression)


if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""The entry point for brain-even game (is random number even)."""


from brain_games.cli import greet
from brain_games.cli import welcome_user
from brain_games.games.even_numbers import even_numbers_game


def main():
    """Run a game."""
    greet()
    name = welcome_user()
    even_numbers_game(name)


if __name__ == '__main__':
    main()

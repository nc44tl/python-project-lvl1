#!/usr/bin/env python

"""The entry point for program."""


from brain_games.cli import welcome_user
from brain_games.cli import greet


def main():
    """Run a program."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()

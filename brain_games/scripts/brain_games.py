#!/usr/bin/env python

"""The entry point for program."""


from brain_games.cli import greet, welcome_user


def main():
    """Run a program."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()

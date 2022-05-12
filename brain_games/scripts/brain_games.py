#!/usr/bin/env python

"""The entry point for program."""


from brain_games.cli import welcome_user


def main():
    """Run a program."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()

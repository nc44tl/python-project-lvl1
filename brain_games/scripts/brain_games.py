#!/usr/bin/env python

"""The entry point for program."""


from brain_games.cli import welcome_user


def greet():
    """Greeting on startup event."""
    print('Welcome to the Brain Games!')


def main():
    """Run a program."""
    greet()
    welcome_user()


if __name__ == '__main__':
    main()

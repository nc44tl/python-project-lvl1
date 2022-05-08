"""CLI interactions with user."""

import prompt


def greet():
    """Greeting on startup event."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """User acquaintance.

    Returns:
        user's name.
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


brain_even_description = 'Answer "yes" if the number is even, \
otherwise answer "no".'
brain_calc_description = 'What is the result of the expression?'
game_select_error = "Sorry, I don't know that game yet"


def print_game_description(game):
    """Print game explanation.

    Parameters:
        game: name of the game
    """
    if game == 'brain-even':
        print(brain_even_description)
        return
    elif game == 'brain-calc':
        print(brain_calc_description)
        return
    else:
        print(game_select_error)


question_string = 'Question: '
answer_prompt = 'Your answer: '


def print_win_phrase(username):
    """Print win phrase.

    Parameters:
        username: user's name
    """
    print('Congratulations, {0}!'.format(username))


def print_loose_phrase(user_answer, correct_answer, username):
    """Print loose phrase.

    Parameters:
        user_answer: user's answer
        correct_answer: correct answer
        username: user's name
    """
    print("'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {user}!".
        format(  # noqa: E128 (intendation)
            user_answer=user_answer,
            correct_answer=correct_answer,
            user=username,
        ),
    )

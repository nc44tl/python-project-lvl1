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


brain_even_description = 'Answer "yes" if the number is even, otherwise answer "no".'
brain_calc_description = 'What is the result of the expression?'
game_select_error = "Sorry, I don't know that game yet"


def get_game_description(game):
    if game == 'brain-even':
        print(brain_even_description)
        return
    elif game == 'brain-calc':
        print(brain_calc_description)
        return
    else:
        print(game_select_error)


question_string = 'Question: '
answer_prompt_string = 'Your answer: '


def get_win_phrase(username):
    print('Congratulations, {0}!'.format(username))

def get_loose_phrase(user_answer, correct_answer, username):
    print("'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {user}!".
                format(
                    user_answer=user_answer,
                    correct_answer=correct_answer,
                    user=username,
                ),
            )

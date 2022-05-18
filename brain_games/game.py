"""General game algorythm."""


import prompt

ROUNDS_PER_GAME = 3


def run_game(game):
    """General game temlplate.

    Parameters:
        game: module with game
    """
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)

    for _ in range(ROUNDS_PER_GAME):
        (case, correct_answer) = game.run_round()
        print(f'Question: {case}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {username}!")
            break

        print('Correct!')

    else:
        print(f'Congratulations, {username}!')

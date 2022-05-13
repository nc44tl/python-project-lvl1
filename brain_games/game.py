"""General game algorythm."""


import prompt

ROUNDS_PER_GAME = 3


def run_game(game):
    """General game temlplate.

    Parameters:
        game: module with game
    """
    print('Welcome to the Brain Games!')
    # TODO после проверки, возможно, убрать ниже дублирование с welcome_user()
    # (dev: 4052e4c). Либо убрать скрипт brain_games и что с ним связано.
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESCRIPTION)

    for _ in range(ROUNDS_PER_GAME):
        (case, correct_answer) = game.run_round()
        print(f'Question: {case}')
        user_answer = prompt.string('Your answer: ')
        res = user_answer == correct_answer

        if not res:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\n\
Let's try again, {username}!")
            break

    else:
        print(f'Congratulations, {username}!')

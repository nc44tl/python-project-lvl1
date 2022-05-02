import prompt
import sys
from random import randint


def get_number():
    return randint(-sys.maxsize, sys.maxsize)


def is_even(number):
    return number % 2 == 0


def check_answer(number, answer):
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (answer == correct_answer, correct_answer)


game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_numbers_game(user):
    print(game_description)
    
    counter = 0

    while counter < 3:
        number = get_number()

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        (result, correct_answer) = check_answer(number, answer)

        if result:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user}!")
            return

    print(f'Congratulations, {user}!')

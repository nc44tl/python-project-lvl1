import prompt


def is_even(number):
    return number % 2 == 0


def check_answer(number, answer):
    return answer == 'no'


game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_numbers_game(user):
    print(game_description)
    
    counter = 0

    while counter < 3:
        number = 25

        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')

        if check_answer(number, answer):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was another answer.\nLet's try again, {user}!")
            return
        
    print(f'Congratulations, {user}!')

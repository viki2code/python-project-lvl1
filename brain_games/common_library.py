"""
Library consists common functions for every games

"""

import prompt
import random

round_count = 3


def welcome():
    return print('Welcome to the Brain Games!')


def get_user_name():
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def game_run(brain_game):
    welcome()
    user_name = get_user_name()
    print(f'Answer "yes" if the number is {brain_game.game_name}\
,otherwise answer "no".')
    for i in range(round_count):
        question_number = random.randint(1, 100)
        print(f'Question: {question_number}')
        game_result = brain_game.get_game_result(question_number)
        user_answer = prompt.string('Your answer: ')
        if game_result == user_answer:
            print('Correct!')
        else:
            return print(f'"{user_answer}" is wrong answer ;(. \
Correct answer was "{game_result}"')
    print(f'Congratulations, {user_name}')

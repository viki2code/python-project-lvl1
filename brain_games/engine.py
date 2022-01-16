"""
Engine for all games

"""

import prompt
from brain_games import const_lib


def run_game(brain_game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(brain_game.TASK)
    for i in range(const_lib.ROUND_COUNT):
        question, game_answer = brain_game.get_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if game_answer == user_answer:
            print('Correct!')
        else:
            return print(f'"{user_answer}" is wrong answer ;(.'
                         f' Correct answer was "{game_answer}"')
    print(f'Congratulations, {user_name}')

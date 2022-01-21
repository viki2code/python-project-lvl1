"""
Engine for all games

"""

import prompt


ROUND_COUNT = 3
QUESTION_USER_NAME = 'May I have your name? '
QUESTION_USER_ANSWER = 'Your answer: '


def run_game(brain_game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string(QUESTION_USER_NAME)
    print(f'Hello, {user_name}!')
    print(brain_game.TASK)
    for i in range(ROUND_COUNT):
        question, game_answer = brain_game.get_game()
        print(f'Question: {question}')
        user_answer = prompt.string(QUESTION_USER_ANSWER)
        if game_answer.lower() == user_answer.lower():
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f' Correct answer was "{game_answer}"')
            return print(f'Let\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')

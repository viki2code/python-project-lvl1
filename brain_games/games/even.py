"""
Game even

"""
import random
from brain_games import const_lib


TASK = 'Answer "yes" if the number is even,otherwise answer "no".'


def is_even(question_number):
    return question_number % 2 == 0


def get_game():
    question_number = random.randint(const_lib.FIRST_RANDOM_VALUE,
                                     const_lib.SECOND_RANDOM_VALUE)
    return question_number, 'yes' if is_even(question_number) else 'no'

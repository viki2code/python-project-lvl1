"""
Game even

"""
import random


TASK = 'Answer "yes" if the number is even,otherwise answer "no".'
FIRST_RANDOM_VALUE = 1
SECOND_RANDOM_VALUE = 50


def is_even(question_number):
    return question_number % 2 == 0


def get_game():
    question_number = random.randint(FIRST_RANDOM_VALUE,
                                     SECOND_RANDOM_VALUE)
    return question_number, 'yes' if is_even(question_number) else 'no'

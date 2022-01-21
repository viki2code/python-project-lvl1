"""
Game prime
"""
import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
FIRST_RANDOM_VALUE = 1
SECOND_RANDOM_VALUE = 50


def is_prime(question_number):
    first_prime = 2
    if question_number < first_prime:
        return False
    for i in range(first_prime, question_number // 2 + 1):
        if question_number % i == 0:
            return False
    return True


def get_game():
    question_number = random.randint(FIRST_RANDOM_VALUE,
                                     SECOND_RANDOM_VALUE)
    return f'{question_number}',\
        'yes' if is_prime(question_number) else 'no'

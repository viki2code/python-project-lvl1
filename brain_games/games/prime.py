"""
Game prime
"""
import random
from brain_games import const_lib


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question_number):
    first_prime = 2
    if question_number < first_prime:
        return False
    for i in range(first_prime, question_number // 2 + 1):
        if question_number % i == 0:
            return False
    return True


def get_game():
    question_number = random.randint(const_lib.FIRST_RANDOM_VALUE,
                                     const_lib.SECOND_RANDOM_VALUE)
    return f'{question_number}',\
        'yes' if is_prime(question_number) else 'no'

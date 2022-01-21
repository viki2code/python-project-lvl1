"""
Game gcd
"""
import random
import math


TASK = 'Find the greatest common divisor of given numbers.'
FIRST_RANDOM_VALUE = 1
SECOND_RANDOM_VALUE = 50


def get_game():
    first_number = random.randint(FIRST_RANDOM_VALUE,
                                  SECOND_RANDOM_VALUE)
    second_number = random.randint(FIRST_RANDOM_VALUE,
                                   SECOND_RANDOM_VALUE)
    return f'{str(first_number)}  {str(second_number)}',\
        f'{math.gcd(first_number, second_number)}'

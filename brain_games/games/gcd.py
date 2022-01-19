"""
Game gcd
"""
import random
from brain_games import const_lib


TASK = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    if first_number == 0:
        return second_number
    return get_gcd(second_number % first_number, first_number)


def get_game():
    first_number = random.randint(const_lib.FIRST_RANDOM_VALUE,
                                  const_lib.SECOND_RANDOM_VALUE)
    second_number = random.randint(const_lib.FIRST_RANDOM_VALUE,
                                   const_lib.SECOND_RANDOM_VALUE)
    return f'{str(first_number)}  {str(second_number)}',\
        f'{get_gcd(first_number, second_number)}'

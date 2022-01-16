"""
Game random calculator
"""
import random
import operator
from brain_games import const_lib


TASK = 'What is the result of the expression?'


def get_game():
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul}
    first_number = random.randint(const_lib.FIRST_RANDOM_VALUE,
                                  const_lib.SECOND_RANDOM_VALUE)
    second_number = random.randint(const_lib.FIRST_RANDOM_VALUE,
                                   const_lib.SECOND_RANDOM_VALUE)
    operation = random.choice(list(operations.keys()))
    return f'{first_number} {operation} {second_number}',\
        f'{operations.get(operation)(first_number,second_number)}'

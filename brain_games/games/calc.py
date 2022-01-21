"""
Game random calculator
"""
import random
import operator


TASK = 'What is the result of the expression?'
FIRST_RANDOM_VALUE = 1
SECOND_RANDOM_VALUE = 50


def get_game():
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul}
    first_number = random.randint(FIRST_RANDOM_VALUE,
                                  SECOND_RANDOM_VALUE)
    second_number = random.randint(FIRST_RANDOM_VALUE,
                                   SECOND_RANDOM_VALUE)
    operation = random.choice(list(operations.keys()))
    return f'{first_number} {operation} {second_number}',\
        f'{operations.get(operation)(first_number,second_number)}'

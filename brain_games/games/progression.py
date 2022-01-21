"""
Game progression
"""
import random


TASK = 'What number is missing in the progression?'
FIRST_RANDOM_VALUE = 1
SECOND_RANDOM_VALUE = 50


def get_progression():
    length_progression = random.randint(5, 10)
    step = random.randint(FIRST_RANDOM_VALUE,
                          SECOND_RANDOM_VALUE)
    start = random.randint(FIRST_RANDOM_VALUE,
                           SECOND_RANDOM_VALUE)
    stop = start + step * length_progression
    return list(range(start, stop, step)), length_progression


def get_game():
    progression, length_progression = get_progression()
    hide_element = random.randint(1, length_progression)
    answer = progression[hide_element]
    progression[hide_element] = '..'
    return ' '.join(str(p) for p in progression),\
           f'{answer}'

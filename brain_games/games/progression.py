"""
Game progression
"""
import random
from brain_games import const_lib


TASK = 'What number is missing in the progression?'


def get_progression():
    length_progression = random.randint(5, 10)
    step = random.randint(const_lib.FIRST_RANDOM_VALUE,
                          const_lib.SECOND_RANDOM_VALUE)
    start = random.randint(const_lib.FIRST_RANDOM_VALUE,
                           const_lib.SECOND_RANDOM_VALUE)
    stop = start + step * length_progression
    return list(range(start, stop, step)), length_progression


def get_game():
    progression, length_progression = get_progression()
    hide_element = random.randint(1, length_progression)
    answer = progression[hide_element]
    progression[hide_element] = '..'
    return ' '.join(str(p) for p in progression),\
           f'{answer}'

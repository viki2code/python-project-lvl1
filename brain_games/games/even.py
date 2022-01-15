"""
Game even

"""


game_name = 'even'


def is_even(question_number):
    return question_number % 2 == 0


def get_game_result(question_number):
    return 'yes' if is_even(question_number) else 'no'

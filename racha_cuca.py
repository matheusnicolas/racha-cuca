import random

TOTAL_FIELDS = 8
MIN_VALUE = 1
MAX_VALUE = 8

def board(values) -> str:
    tab = """
    |  {}   {}   {}  |
    |             |
    |  {}   {}   {}  |
    |             |
    |  {}   {}   X  |
    """.format(*values)
    return tab

def board_values_generator() -> []:
    values_stored = []
    while len(values_stored) != TOTAL_FIELDS:
        raffled_value = random.randint(MIN_VALUE, MAX_VALUE)
        if raffled_value not in values_stored:
            values_stored.append(raffled_value)
        del raffled_value
    return values_stored

print(board(board_values_generator()))

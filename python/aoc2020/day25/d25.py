import re
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class ComboBreaker:
    def __init__(self, filename):
        self.public_keys = [int(n) for n in re.findall(r"[+-]?\d+", Path(filename).read_text())]

    def encryption_key(self):
        card_public_key, door_public_key = self.public_keys
        card_loop_size = door_loop_size = 0
        m = 20201227
        value = 1
        for counter in count(1):
            value = (value * 7) % m
            if value == card_public_key and card_loop_size == 0:
                card_loop_size = counter
            if value == door_public_key and door_loop_size == 0:
                door_loop_size = counter
            if card_loop_size and door_loop_size:
                break
        assert pow(door_public_key, card_loop_size, m) == pow(card_public_key, door_loop_size, m)
        return pow(door_public_key, card_loop_size, m)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ComboBreaker("sample1.txt").encryption_key() == 14897079

    print("Tests passed, starting with the puzzle")

    puzzle = ComboBreaker(data.input_file)

    print(puzzle.encryption_key())

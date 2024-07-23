import re
from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data


class TwoFactorAuthentication:
    def __init__(self, filename):
        self.screen = defaultdict(bool)
        for line in Path(filename).read_text().splitlines():
            a, b = list(map(int, re.findall(r"-?\d+", line)))
            if line.startswith("rect"):
                for i, j in product(range(a), range(b)):
                    self.screen[(i, j)] = True
            elif line.startswith("rotate row"):
                row = [self.screen[(i, a)] for i in range(50)]
                for i in range(50):
                    self.screen[(i, a)] = row[(i - b) % 50]
            elif line.startswith("rotate column"):
                col = [self.screen[(a, i)] for i in range(6)]
                for i in range(6):
                    self.screen[(a, i)] = col[(i - b) % 6]

    def lit_led_count(self):
        return sum(self.screen.values())

    def print_code(self):
        for i, j in product(range(6), range(50)):
            print("#" if self.screen[(j, i)] else " ", end="" if j < 49 else "\n")


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TwoFactorAuthentication("sample1.txt").lit_led_count() == 6

    print("Tests passed, starting with the puzzle")

    puzzle = TwoFactorAuthentication(data.input_file)

    print(puzzle.lit_led_count())
    puzzle.print_code()

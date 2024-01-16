import os
from pathlib import Path


class MineCartMadness:
    def __init__(self, filename):
        self.direction = ((-1, 0), (0, -1), (1, 0), (0, 1))
        self.direction_codes = {"<": 0, "^": 1, ">": 2, "v": 3}
        self.lines = Path(filename).read_text().split("\n")
        self.process_lines()
        self.first_crash = None
        self.simulate()

    def process_lines(self):
        self.map = dict()
        self.carts = []
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                if ch in self.direction_codes.keys():
                    dir = self.direction_codes[ch]
                    self.carts.append(((col, row), dir, -1))
                    ch = "-" if ch in "<>" else "|"
                self.map[(col, row)] = ch

    def simulate(self):
        carts = self.carts.copy()
        while len(carts) > 1:
            new_carts = []
            current_locations = set()
            for cart in sorted(carts, key=lambda x: x[0]):
                pre_loc, dir, state = cart
                loc = tuple([pre_loc[i] + self.direction[dir][i] for i in range(2)])
                for p in [pre_loc, loc]:
                    if p in current_locations:
                        new_carts = [c for c in new_carts if c[0] != p]
                        if self.first_crash is None:
                            self.first_crash = p
                        break
                else:
                    current_locations.add(loc)
                    ch = self.map[loc]
                    if ch == "+":
                        dir = (dir + state) % 4
                        state = (state + 2) % 3 - 1
                    elif ch == "\\":
                        dir = {0: 1, 1: 0, 2: 3, 3: 2}[dir]
                    elif ch == "/":
                        dir = {0: 3, 1: 2, 2: 1, 3: 0}[dir]
                    new_carts.append((loc, dir, state))
            carts = new_carts
        if carts:
            self.last_cart = carts.pop()[0]


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = MineCartMadness(filename)
    assert answer1 is None or test.first_crash == answer1
    assert answer2 is None or test.last_cart == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", (7, 3), None)
    test_samples("sample2.txt", None, (6, 4))

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day13.txt'
    puzzle = MineCartMadness(input_file)
    print(puzzle.first_crash)
    print(puzzle.last_cart)

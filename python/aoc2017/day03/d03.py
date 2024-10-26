from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class SpiralMemory:
    def __init__(self, input):
        self.input = input if isinstance(input, int) else int(Path(input).read_text().strip())
        self.dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        self.mask8 = [[i, j] for i in range(-1, 2) for j in range(-1, 2) if i or j]

    def print(self, m: dict):
        k = m.keys()
        xs = {xy[0] for xy in k}
        ys = {xy[1] for xy in k}
        for y in range(min(ys), max(ys) + 1):
            for x in range(min(xs), max(xs) + 1):
                print(f"{m.get((x,y),0):6}", end="")
            print()
        print("-----------------")

    def simple_spiral(self):
        counter = 1
        step = 0
        x, y = 0, 0
        map = {(x, y): counter}
        while True:
            step += 1
            x += 1
            y += 1
            for dx, dy in self.dirs:
                for _ in range(step * 2):
                    counter += 1
                    x += dx
                    y += dy
                    map[(x, y)] = counter
                    # self.print(m)
                    if counter == self.input:
                        return abs(x) + abs(y)

    def summation_spiral(self):
        step = 0
        x, y = 0, 0
        m = defaultdict(int)
        m[(x, y)] = 1
        while True:
            step += 1
            x += 1
            y += 1
            for dx, dy in self.dirs:
                for _ in range(step * 2):
                    x += dx
                    y += dy
                    value = sum([m[(x + xn, y + yn)] for xn, yn in self.mask8])
                    # self.print(m)
                    if value > self.input:
                        return value
                    m[(x, y)] = value


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = SpiralMemory(filename)
    assert test.simple_spiral() == answer1 or answer1 is None
    assert test.summation_spiral() == answer2 or answer2 is None


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples(12, 3, None)
    test_samples(23, 2, None)
    test_samples(1024, 31, None)

    print("Tests passed, starting with the puzzle")

    puzzle = SpiralMemory(data.input_file)
    print(puzzle.simple_spiral())
    print(puzzle.summation_spiral())

import os
from collections import deque
from functools import reduce
from pathlib import Path


class KnotHash:
    def __init__(self, filename=None, input=None):
        self.input = Path(filename).read_text().strip() if filename else input

    def do(self, input_lengths):
        for i in input_lengths:
            self.elements.rotate(-self.head)
            buffer = []
            for _ in range(i):
                buffer.append(self.elements.popleft())
            for item in buffer:
                self.elements.appendleft(item)
            self.elements.rotate(self.head)
            self.head = (self.head + i + self.skip) % len(self.elements)
            self.skip += 1

    def single_knot_hash(self, ar_len=256):
        input_lengths = list(map(int, self.input.split(",")))
        self.elements = deque(range(ar_len))
        self.head = self.skip = 0
        self.do(input_lengths)
        return self.elements[0] * self.elements[1]

    def full_knot_hash(self):
        input = list(map(ord, self.input)) + [17, 31, 73, 47, 23]
        self.elements = deque(range(256))
        self.head = self.skip = 0
        for _ in range(64):
            self.do(input)
        elements_list = list(self.elements)
        rs = [reduce(lambda a, b: a ^ b, elements_list[i * 16 : (i + 1) * 16]) for i in range(16)]
        return "".join([(hex(r)[2:]).rjust(2, "0") for r in rs])


def test_samples(filename, answer1, answer2, array_len=256):
    if answer1 is None and answer2 is None:
        return
    test = KnotHash(filename)
    assert answer1 is None or test.single_knot_hash(array_len) == answer1
    assert answer2 is None or test.full_knot_hash() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 12, None, 5)
    test_samples("sample2.txt", None, "a2582a3a0e66e6e86e3812dcb672a272")
    test_samples("sample3.txt", None, "33efeb34ea91902bb2f59c9920caa6cd")
    test_samples("sample4.txt", None, "3efbe78a8d82f29979031a4aa0b16a9d")
    test_samples("sample5.txt", None, "63960835bcdc130f0b66d7ff4f6a5a8e")

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2017_day10.txt'
    puzzle = KnotHash(input_file)
    print(puzzle.single_knot_hash())
    print(puzzle.full_knot_hash())

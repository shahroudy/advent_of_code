import os
from functools import cache
from pathlib import Path


class LensLibrary:
    def __init__(self, filename):
        self.words = Path(filename).read_text().strip().split(",")
        self.boxes = [[] for _ in range(256)]

    @cache
    def hash(self, word):
        value = 0
        for ch in word:
            value = (value + ord(ch)) * 17 % 256
        return value

    def input_hash(self):
        return sum(self.hash(word) for word in self.words)

    def find_lens_in_box(self, box, label):
        for i, b in enumerate(box):
            if b[0] == label:
                return i
        return -1

    def remove_lens(self, label):
        box = self.hash(label)
        index = self.find_lens_in_box(self.boxes[box], label)
        if index >= 0:
            self.boxes[box] = self.boxes[box][:index] + self.boxes[box][index + 1 :]

    def insert_lens(self, label, value):
        box = self.hash(label)
        index = self.find_lens_in_box(self.boxes[box], label)
        if index >= 0:
            self.boxes[box][index] = (label, value)
        else:
            self.boxes[box].append((label, value))

    def focusing_power(self):
        return sum(
            sum((bi + 1) * (li + 1) * int(value) for li, (_, value) in enumerate(box))
            for bi, box in enumerate(self.boxes)
        )

    def focusing_power_after_HASHMAP_lens_configuration(self):
        for word in self.words:
            if "-" in word:
                self.remove_lens(word[:-1])
            elif "=" in word:
                self.insert_lens(*word.split("="))

        return self.focusing_power()


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = LensLibrary(filename)
    assert answer1 is None or test.input_hash() == answer1
    assert answer2 is None or test.focusing_power_after_HASHMAP_lens_configuration() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 52, None)
    test_samples("sample2.txt", 1320, 145)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day15.txt'
    puzzle = LensLibrary(input_file)
    print(puzzle.input_hash())
    print(puzzle.focusing_power_after_HASHMAP_lens_configuration())

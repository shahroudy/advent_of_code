import os
import re
from pathlib import Path


class DigitalPlumber:
    def __init__(self, filename):
        self.pipes = {}
        for line in Path(filename).read_text().strip().split("\n"):
            nums = list(map(int, re.findall(r"\d+", line)))
            self.pipes[nums[0]] = nums[1:]

    def find_connected_ids(self, id):
        new_nodes = {id}
        connected = {id}
        while new_nodes:
            current = new_nodes.pop()
            for next in self.pipes[current]:
                if next not in connected:
                    new_nodes.add(next)
                    connected.add(next)
        return connected

    def group_size_of_zero(self):
        return len(self.find_connected_ids(0))

    def group_count(self):
        count = 0
        rem = set(self.pipes.keys())
        while rem:
            picked = rem.pop()
            count += 1
            rem -= self.find_connected_ids(picked)
        return count


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = DigitalPlumber(filename)
    assert answer1 is None or test.group_size_of_zero() == answer1
    assert answer2 is None or test.group_count() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 6, 2)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2017_day12.txt'
    puzzle = DigitalPlumber(input_file)
    print(puzzle.group_size_of_zero())
    print(puzzle.group_count())

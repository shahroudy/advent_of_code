import os
from pathlib import Path
from myutils.io_handler import get_input_data


class AMazeofTwistyTrampolinesAllAlike:
    def __init__(self, filename):
        self.offsets = list(map(int, Path(filename).read_text().strip().split("\n")))

    def jump_count(self, strange):
        offsets = self.offsets.copy()
        head, count = 0, 0
        while 0 <= head < len(offsets):
            count += 1
            new_head = head + offsets[head]
            if strange and offsets[head] >= 3:
                offsets[head] -= 1
            else:
                offsets[head] += 1
            head = new_head
        return count

    def simple_jumps(self):
        return self.jump_count(strange=False)

    def strange_jumps(self):
        return self.jump_count(strange=True)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = AMazeofTwistyTrampolinesAllAlike(filename)
    assert test.simple_jumps() == answer1 or answer1 is None
    assert test.strange_jumps() == answer2 or answer2 is None


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 5, 10)

    print("Tests passed, starting with the puzzle")

    puzzle = AMazeofTwistyTrampolinesAllAlike(data.input_file)
    print(puzzle.simple_jumps())
    print(puzzle.strange_jumps())

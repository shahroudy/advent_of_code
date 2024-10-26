from pathlib import Path

from aoc2017.day10.d10 import KnotHash
from myutils.io_handler import get_input_data


class DiskDefragmentation:
    def __init__(self, filename):
        key_string = Path(filename).read_text().strip()
        ones = set()
        for i in range(128):
            hash = KnotHash(input=key_string + f"-{i}").full_knot_hash()
            binary_128 = bin(int(hash, 16))[2:].rjust(128, "0")
            for j, c in enumerate(binary_128):
                if c == "1":
                    ones.add((i, j))
        self.one_count = len(ones)
        self.region_count = 0
        while ones:
            to_process = [ones.pop()]
            self.region_count += 1
            while to_process:
                i, j = to_process.pop()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    n = (i + dx, j + dy)
                    if n in ones:
                        ones.remove(n)
                        to_process.append(n)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = DiskDefragmentation(filename)
    assert answer1 is None or test.one_count == answer1
    assert answer2 is None or test.region_count == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 8108, 1242)

    print("Tests passed, starting with the puzzle")

    puzzle = DiskDefragmentation(data.input_file)

    print(puzzle.one_count)
    print(puzzle.region_count)

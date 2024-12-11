from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class AdapterArray:
    def __init__(self, filename):
        adapters = sorted(list(map(int, Path(filename).read_text().splitlines())))
        self.adapters = adapters + [adapters[-1] + 3]

    def difference_count_multiplications(self):
        diff_counter = defaultdict(int)
        for i, j in zip([0] + self.adapters[:-1], self.adapters):
            diff_counter[j - i] += 1
        return diff_counter[1] * diff_counter[3]

    def count_all_possible_ways(self):
        ways = defaultdict(int)
        ways[0] = 1
        for i in self.adapters:
            ways[i] = sum(ways[i - 1 - j] for j in range(3))
        return ways[i]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert AdapterArray("sample1.txt").difference_count_multiplications() == 35
    assert AdapterArray("sample2.txt").difference_count_multiplications() == 220
    assert AdapterArray("sample1.txt").count_all_possible_ways() == 8
    assert AdapterArray("sample2.txt").count_all_possible_ways() == 19208

    print("Tests passed, starting with the puzzle")

    puzzle = AdapterArray(data.input_file)

    print(puzzle.difference_count_multiplications())
    print(puzzle.count_all_possible_ways())

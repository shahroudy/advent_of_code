import re
from collections import Counter
from pathlib import Path

from myutils.io_handler import get_input_data


class Lanternfish:
    def __init__(self, filename):
        self.nums = list(map(int, re.findall(r"(\d+)", Path(filename).read_text())))

    def lanternfish_count(self, days):
        count = Counter(self.nums)
        for _ in range(days):
            count = {age: count[(age + 1) % 9] for age in range(9)}
            count[6] += count[8]
        return sum(count.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Lanternfish("sample1.txt").lanternfish_count(18) == 26
    assert Lanternfish("sample1.txt").lanternfish_count(80) == 5934
    assert Lanternfish("sample1.txt").lanternfish_count(256) == 26984457539

    print("Tests passed, starting with the puzzle")

    puzzle = Lanternfish(data.input_file)
    print(puzzle.lanternfish_count(80))
    print(puzzle.lanternfish_count(256))

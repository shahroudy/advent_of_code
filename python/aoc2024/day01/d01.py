import re
from pathlib import Path

from myutils.io_handler import get_input_data


class HistorianHysteria:
    def __init__(self, filename):
        values = list(map(int, re.findall(r"-?\d+", Path(filename).read_text())))
        self.left, self.right = [sorted(values[i::2]) for i in range(2)]

    def total_distance(self):
        return sum(abs(i - j) for i, j in zip(self.left, self.right))

    def similarity_score(self):
        return sum(i * self.right.count(i) for i in self.left)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert HistorianHysteria("sample1.txt").total_distance() == 11
    assert HistorianHysteria("sample1.txt").similarity_score() == 31

    print("Tests passed, starting with the puzzle")

    puzzle = HistorianHysteria(data.input_file)

    print(puzzle.total_distance())
    print(puzzle.similarity_score())

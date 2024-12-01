from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import multiply


class TobogganTrajectory:
    def __init__(self, filename):
        self.trees = set()
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                if ch == "#":
                    self.trees.add((col, row))
        self.rows, self.cols = row + 1, col + 1

    def tree_count(self, dx=3, dy=1):
        x = y = result = 0
        while y < self.rows:
            result += (x % self.cols, y) in self.trees
            x += dx
            y += dy
        return result

    def multiplication_of_tree_counts_for_all_slopes(self):
        return multiply(self.tree_count(*d) for d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TobogganTrajectory("sample1.txt").tree_count() == 7
    assert TobogganTrajectory("sample1.txt").multiplication_of_tree_counts_for_all_slopes() == 336

    print("Tests passed, starting with the puzzle")

    puzzle = TobogganTrajectory(data.input_file)

    print(puzzle.tree_count())
    print(puzzle.multiplication_of_tree_counts_for_all_slopes())

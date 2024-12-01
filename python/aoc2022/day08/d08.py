import os
from collections import defaultdict
from pathlib import Path
from myutils.io_handler import get_input_data


class TreetopTreeHouse:
    def __init__(self, filename):
        self.map = {}
        lines = Path(filename).read_text().strip().split("\n")
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = int(ch)
        self.rows = len(lines)
        self.cols = len(lines[0])

    def trees_visible_from_outside(self):
        visible = set()

        for y in range(0, self.rows):
            # count from the left of each row
            max_height = -1
            for x in range(0, self.cols):
                height = self.map[(x, y)]
                if height > max_height:
                    max_height = height
                    visible.add((x, y))
            # count from the right of each row
            max_height = -1
            for x in range(self.cols - 1, -1, -1):
                height = self.map[(x, y)]
                if height > max_height:
                    max_height = height
                    visible.add((x, y))
        for x in range(0, self.cols):
            # count from the top of each col
            max_height = -1
            for y in range(0, self.rows):
                height = self.map[(x, y)]
                if height > max_height:
                    max_height = height
                    visible.add((x, y))
            # count from the bottom of each col
            max_height = -1
            for y in range(self.rows - 1, -1, -1):
                height = self.map[(x, y)]
                if height > max_height:
                    max_height = height
                    visible.add((x, y))

        return len(visible)

    def highest_scenic_score(self):
        max_scenic_score = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for x in range(self.cols):
            for y in range(self.cols):
                height = self.map[(x, y)]
                scenic_score = 1
                for delta in directions:
                    visible_trees = 0
                    py, px = y + delta[0], x + delta[1]
                    while px >= 0 and py >= 0 and px < self.cols and py < self.rows:
                        visible_trees += 1
                        if self.map[(px, py)] < height:
                            py += delta[0]
                            px += delta[1]
                        else:
                            break
                    scenic_score *= visible_trees
                max_scenic_score = max(max_scenic_score, scenic_score)
        return max_scenic_score


def test_samples(filename, answer1, answer2):
    test = TreetopTreeHouse(filename)
    assert test.trees_visible_from_outside() == answer1
    assert test.highest_scenic_score() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 21, 8)

    puzzle = TreetopTreeHouse(data.input_file)
    print(puzzle.trees_visible_from_outside())
    print(puzzle.highest_scenic_score())

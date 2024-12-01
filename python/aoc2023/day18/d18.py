import os
from pathlib import Path
from myutils.io_handler import get_input_data


class LavaductLagoon:
    def __init__(self, filename):
        self.inp = []
        for line in Path(filename).read_text().strip().splitlines():
            direction, meters, color = line.split()
            self.inp.append([direction, int(meters), color[2:-1]])

    def count_inner_tiles(self, corners):
        columns = sorted(corners.keys())
        counter = 0
        range_start = pre_corner = 0
        inside = False
        for col in columns:
            corner = corners[col]
            if corner:
                if pre_corner == 0:
                    if inside:
                        counter += col - range_start
                    pre_corner = corner
                    range_start = col
                else:
                    counter += (col - range_start) + 1
                    if pre_corner != corner:
                        inside = not inside
                    if inside:
                        counter -= 1
                        range_start = col
                    pre_corner = 0
            else:  # non-corner, vertical line
                if inside:
                    counter += (col - range_start) + 1
                else:
                    range_start = col
                inside = not inside
        return counter

    def digged_area(self, swapped=False):
        vertical_lines = []
        directions = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
        code_directions = "RDLU"

        rows = {0}  # rows that may have different inner tiles than its neighbors
        x, y = 0, 0
        for dir, meters, color in self.inp:
            if swapped:
                dir = code_directions[int(color[-1])]
                meters = int(color[:-1], 16)
            dx, dy = directions[dir]
            nx, ny = x + dx * meters, y + dy * meters
            if dir in "UD":
                vertical_lines.append((x, y, ny) if y < ny else (x, ny, y))
            x, y = nx, ny
            rows |= {y, y - 1}

        rows = sorted(rows)
        total_dug = 0
        pre_row = None
        for pre_row, row in zip(rows[:-1], rows[1:]):
            corners = dict()
            for col, top_row, bottom_row in vertical_lines:
                if top_row == row:
                    corners[col] = 1
                elif bottom_row == row:
                    corners[col] = -1
                elif top_row < row < bottom_row:
                    corners[col] = 0
            total_dug += self.count_inner_tiles(corners) * (row - pre_row)
        return total_dug


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = LavaductLagoon(filename)
    assert answer1 is None or test.digged_area() == answer1
    assert answer2 is None or test.digged_area(swapped=True) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 62, 952408144115)

    print("Tests passed, starting with the puzzle")

    puzzle = LavaductLagoon(data.input_file)
    print(puzzle.digged_area())
    print(puzzle.digged_area(swapped=True))

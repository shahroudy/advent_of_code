import os
from itertools import product
from pathlib import Path
from myutils.io_handler import get_input_data


class StepCounter:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().splitlines()
        self.mask4 = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.map = dict()
        for row, line in enumerate(self.lines):
            for col, ch in enumerate(line):
                if ch == "S":
                    self.start = (col, row)
                    ch = "."
                self.map[(col, row)] = ch
        self.rows, self.cols = row + 1, col + 1
        self.calculate_distance_maps()

    def calculate_distance_maps(self):
        from_center_tiles = {self.start}
        self.dist_to_center = {self.start: 0}
        from_corners_tiles = {
            (0, 0),
            (0, self.rows - 1),
            (self.cols - 1, 0),
            (self.cols - 1, self.rows - 1),
        }
        self.dist_to_corners = {corner: 0 for corner in from_corners_tiles}
        iter = 0
        while from_center_tiles or from_corners_tiles:
            iter += 1
            next_from_center_tiles = set()
            for item in from_center_tiles:
                x, y = item
                for dx, dy in self.mask4:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in self.map:
                        continue
                    if self.map[(nx, ny)] == ".":
                        if (nx, ny) not in self.dist_to_center.keys():
                            next_from_center_tiles.add((nx, ny))
                            self.dist_to_center[(nx, ny)] = iter
            from_center_tiles = next_from_center_tiles

            next_from_corner_tiles = set()
            for item in from_corners_tiles:
                x, y = item
                for dx, dy in self.mask4:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in self.map:
                        continue
                    if self.map[(nx, ny)] == ".":
                        if (nx, ny) not in self.dist_to_corners:
                            next_from_corner_tiles.add((nx, ny))
                            self.dist_to_corners[(nx, ny)] = iter
            from_corners_tiles = next_from_corner_tiles

    def simple_garden_plots_count(self, steps):  # only works for steps within a single map
        return sum(d % 2 == steps % 2 and d <= steps for d in self.dist_to_center.values())

    def garden_plots_in_indefinite_map(self, iterations):
        # even/odd tile counts in corner triangle sections
        odd_count = even_count = odd_tiles_to_subtract = even_tiles_to_add = 0
        for row, col in product(range(self.rows), range(self.cols)):
            if self.map[(col, row)] == "." and (col, row) in self.dist_to_center:
                if (col + row) % 2 == 1:
                    odd_count += 1
                    if self.dist_to_center[(col, row)] > 65:
                        odd_tiles_to_subtract -= 1
                else:
                    even_count += 1
                    if self.dist_to_corners[(col, row)] < 65:
                        even_tiles_to_add += 1

        radius = (iterations - 65) // 131
        assert (iterations - 65) % 131 == 0
        assert iterations % 2 == 1

        sum = (radius + 1) * odd_tiles_to_subtract + radius * (even_tiles_to_add)
        row_tiles = odd_count
        for row in range(radius):
            sum += row_tiles * 2
            row_tiles += even_count + odd_count
        sum += row_tiles
        return sum


if __name__ == "__main__":
    data = get_input_data(__file__)
    test = StepCounter("sample1.txt")
    assert test.simple_garden_plots_count(steps=6) == 16

    print("Tests passed, starting with the puzzle")

    puzzle = StepCounter(data.input_file)
    print(puzzle.simple_garden_plots_count(steps=64))
    print(puzzle.garden_plots_in_indefinite_map(iterations=26501365))

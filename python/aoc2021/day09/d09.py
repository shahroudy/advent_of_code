import os
from numpy import product
from collections import defaultdict
from myutils.file_reader import read_lines


class SmokeBasin:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.process()

    def process(self):
        row = 0
        self.map = defaultdict(lambda: 9)
        self.rows, self.cols = 0, 0
        for line in self.lines:
            col = 0
            for ch in line:
                self.map[(row, col)] = int(ch)
                col += 1
            if row == 0:
                self.cols = col
            col = 0
            row += 1
        self.rows = row

        self.mask = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def low_points(self):
        sum = 0
        for row in range(self.rows):
            for col in range(self.cols):
                current = self.map[(row, col)]
                for n in self.mask:
                    neighbor = self.map[(row + n[0], col + n[1])]
                    if neighbor <= current:
                        break
                else:
                    sum += current + 1
        return sum

    def largest_basins(self):
        basin_sizes = list()

        found = True
        while found:
            found = False
            for start_row in range(self.rows):
                for start_col in range(self.cols):
                    if self.map[(start_row, start_col)] != 9:
                        found = True
                        break
                if found:
                    break
            else:
                break

            stack = [(start_row, start_col)]
            self.map[(start_row, start_col)] = 9
            curbassize = 1
            while stack:
                current_row, current_col = stack.pop()
                for n in self.mask:
                    neighbor_loc = (current_row + n[0], current_col + n[1])
                    if self.map[neighbor_loc] != 9:
                        stack.append(neighbor_loc)
                        self.map[neighbor_loc] = 9
                        curbassize += 1
            basin_sizes.append(curbassize)

        basin_sizes.sort(reverse=True)
        return product(basin_sizes[0:3])


if __name__ == "__main__":
    test1 = SmokeBasin("test1.txt")
    assert test1.low_points() == 15
    assert test1.largest_basins() == 1134

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day09.txt'
    smoke_basin = SmokeBasin(input_file)
    print(smoke_basin.low_points())
    print(smoke_basin.largest_basins())

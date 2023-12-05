import os
from myutils.file_reader import read_lines


class DumboOctopus:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.process()

    def process(self):
        self.map = dict()
        row = 0
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

    def analyse_flashes(self):
        flash_count = 0
        sync_flash_step = 0
        step = 0
        while step < 100 or not sync_flash_step:
            step += 1
            flashing = set()
            flashed = set()
            for i in range(self.rows):
                for j in range(self.cols):
                    self.map[(i, j)] += 1
                    if self.map[(i, j)] > 9:
                        flashing.add((i, j))
            while flashing:
                f = flashing.pop()
                flashed.add(f)
                if step <= 100:
                    flash_count += 1
                i, j = f

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        n = (x, y)
                        if n in self.map:
                            self.map[n] += 1
                            if self.map[n] > 9:
                                if n not in flashed:
                                    flashing.add(n)

            if not sync_flash_step and len(flashed) == self.rows * self.cols:
                sync_flash_step = step

            for f in flashed:
                self.map[f] = 0

        return flash_count, sync_flash_step


if __name__ == "__main__":
    test1 = DumboOctopus("test1.txt")
    assert test1.analyse_flashes() == (1656, 195)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day11.txt'
    dumbo_octopus = DumboOctopus(input_file)
    print(dumbo_octopus.analyse_flashes())

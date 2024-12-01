import os
from myutils.file_reader import read_line_groups


class TrenchMap:
    def __init__(self, filename):
        self.line_groups = read_line_groups(filename)
        self.process()

    def process(self):
        self.code = []
        for ch in self.line_groups[0][0]:
            self.code.append(1 if ch == "#" else 0)

        self.init_image = set()
        row = 0
        for line in self.line_groups[1]:
            col = 0
            for ch in line:
                if ch == "#":
                    self.init_image.add((row, col))
                col += 1
            if row == 0:
                cols = col
            col = 0
            row += 1
        rows = row

        self.minrow, self.maxrow = 0, rows
        self.mincol, self.maxcol = 0, cols

        self.default_value = 0
        self.mask9 = [[i, j] for i in range(-1, 2) for j in range(-1, 2)]

    def enhance(self):
        newimage = set()
        for row in range(self.minrow - 1, self.maxrow + 1):
            for col in range(self.mincol - 1, self.maxcol + 1):
                sum = 0
                for n in self.mask9:
                    nr, nc = row + n[0], col + n[1]
                    if self.minrow <= nr < self.maxrow and self.mincol <= nc < self.maxcol:
                        pixel = 1 if (nr, nc) in self.image else 0
                    else:
                        pixel = self.default_value
                    sum = sum * 2 + pixel
                if self.code[sum]:
                    newimage.add((row, col))

        if self.default_value:
            self.default_value = self.code[-1]  # code for 111111111
        else:
            self.default_value = self.code[0]  # code for 000000000

        self.minrow -= 1
        self.maxrow += 1
        self.mincol -= 1
        self.maxcol += 1

        self.image = newimage

    def iterative_enhancement(self, times):
        self.image = self.init_image.copy()
        for _ in range(times):
            self.enhance()
        return len(self.image)


if __name__ == "__main__":

    test1 = TrenchMap("test1.txt")
    assert test1.iterative_enhancement(2) == 35
    assert test1.iterative_enhancement(50) == 3351

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day20.txt'
    trench_map = TrenchMap(input_file)
    print(trench_map.iterative_enhancement(2))
    print(trench_map.iterative_enhancement(50))

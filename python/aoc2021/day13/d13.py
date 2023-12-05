import os
from myutils.file_reader import read_line_groups


class TransparentOrigami:
    def __init__(self, filename):
        self.line_groups = read_line_groups(filename)
        self.process()

    def process(self):
        self.dots = set()
        for line in self.line_groups[0]:
            x, y = line.split(",")
            self.dots.add((int(x), int(y)))

        self.folds = []
        for line in self.line_groups[1]:
            parts = line.split()
            p2 = parts[2].split("=")
            self.folds.append((p2[0], int(p2[1])))

    def print_origami(self):
        max_x, max_y = 0, 0
        for x, y in self.dots:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x, y) in self.dots:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print()

    def fold(self, fold_direction, fold_position):
        new_dots = set()
        for x, y in self.dots:
            if fold_direction == "x":
                if x == fold_position:
                    continue
                xn = (
                    x
                    if x < fold_position
                    else fold_position - (x - fold_position)
                )
            else:
                xn = x
            if fold_direction == "y":
                if y == fold_position:
                    continue
                yn = (
                    y
                    if y < fold_position
                    else fold_position - (y - fold_position)
                )
            else:
                yn = y
            new_dots.add((xn, yn))
        self.dots = new_dots

    def foldings(self):
        after_first_fold = -1
        for fold in self.folds:
            self.fold(*fold)
            if after_first_fold < 0:
                after_first_fold = len(self.dots)

        self.print_origami()
        return after_first_fold


if __name__ == "__main__":

    test1 = TransparentOrigami("test1.txt")
    assert test1.foldings() == 17

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day13.txt'
    origami = TransparentOrigami(input_file)
    print(origami.foldings())

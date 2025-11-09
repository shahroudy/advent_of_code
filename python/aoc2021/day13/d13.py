from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.utils import find_all_re


class TransparentOrigami:
    def __init__(self, filename):
        text = Path(filename).read_text()
        self.points = [Point(int(x), int(y)) for x, y in find_all_re(r"(\d+),(\d+)", text)]
        self.folds = [(ax, int(val)) for ax, val in find_all_re(r"fold along (x|y)=(\d+)", text)]

    def fold_value(self, value, fold_at):
        return fold_at - (value - fold_at) if value > fold_at else value

    def fold_point(self, point, fold):
        axis, value = fold
        return Point(
            self.fold_value(point.x, value) if axis == "x" else point.x,
            self.fold_value(point.y, value) if axis == "y" else point.y,
        )

    def fold_points(self, points, fold):
        return set(self.fold_point(p, fold) for p in points)

    def point_count_after_first_fold(self):
        return len(self.fold_points(self.points, self.folds[0]))

    def get_code_from_points(self, points):
        lines = []
        max_x, max_y = 1 + max(p.x for p in points), 1 + max(p.y for p in points)
        for y in range(max_y):
            lines.append("".join(["#" if Point(x, y) in points else "." for x in range(max_x)]))
        return "\n".join(lines)

    def code_after_all_folds(self):
        points = set(self.points)
        for fold in self.folds:
            points = self.fold_points(points, fold)
        return self.get_code_from_points(points)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = TransparentOrigami("sample1.txt")
    assert test.point_count_after_first_fold() == 17
    assert test.code_after_all_folds() == "#####\n#...#\n#...#\n#...#\n#####"

    print("Tests passed, starting with the puzzle")

    puzzle = TransparentOrigami(data.input_file)

    print(puzzle.point_count_after_first_fold())
    print(puzzle.code_after_all_folds())

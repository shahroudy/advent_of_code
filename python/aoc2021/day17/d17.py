from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import read_ints


class TrickShot:
    def __init__(self, filename):
        x0, x1, y0, y1 = read_ints(Path(filename).read_text())
        self.highest_y = 0
        self.shot_count = 0

        d0x_range = range(int((-1 + (1 + 8 * x0) ** 0.5) / 2), x1 + 1)
        d0y_range = range(min(y0, y1), max(abs(y0), abs(y1)) + 1)
        for d0x, d0y in product(d0x_range, d0y_range):
            x, y, dx, dy, current_max_y = 0, 0, d0x, d0y, 0
            while y > y0:
                if dx == 0:
                    if not x0 <= x <= x1:
                        break
                else:
                    x += dx
                    dx -= 1
                y += dy
                dy -= 1
                current_max_y = max(current_max_y, y)
                if x0 <= x <= x1 and y0 <= y <= y1:
                    self.highest_y = max(self.highest_y, current_max_y)
                    self.shot_count += 1
                    break


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = TrickShot("sample1.txt")
    assert test.highest_y == 45
    assert test.shot_count == 112

    print("Tests passed, starting with the puzzle")

    puzzle = TrickShot(data.input_file)

    print(puzzle.highest_y)
    print(puzzle.shot_count)

import re
from pathlib import Path

from myutils.io_handler import get_input_data


class LetItSnow:
    def __init__(self, filename=None):
        if filename:
            self.pos = [int(n) for n in re.findall(r"\d+", Path(filename).read_text())]

    def find_code(self, pos=None):
        row, col = pos or self.pos
        diag = row + col - 1
        order = diag * (diag - 1) // 2 + col
        return 20151125 * pow(252533, order - 1, 33554393) % 33554393


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = LetItSnow()
    assert test.find_code([2, 1]) == 31916031
    assert test.find_code([1, 2]) == 18749137
    assert test.find_code([5, 5]) == 9250759
    assert test.find_code([6, 6]) == 27995004

    print("Tests passed, starting with the puzzle")

    puzzle = LetItSnow(data.input_file)
    print(puzzle.find_code())

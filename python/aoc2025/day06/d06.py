from itertools import groupby
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.matrix import transpose
from myutils.utils import multiply


class TrashCompactor:
    def __init__(self, filename):
        text = Path(filename).read_text().splitlines()
        self.ops = text[-1].replace(" ", "").strip()
        self.numeric_lines = text[:-1]

    def grand_total(self, cephalopod_math):
        if not cephalopod_math:
            m = transpose([[int(n) for n in line.split()] for line in self.numeric_lines])
        else:
            t = [n.strip() for n in transpose(self.numeric_lines)]
            m = [[int(n) for n in g] for k, g in groupby(t, key=lambda x: x == "") if not k]
        return sum(sum(row) if op == "+" else multiply(row) for op, row in zip(self.ops, m))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TrashCompactor("sample1.txt").grand_total(cephalopod_math=False) == 4277556
    assert TrashCompactor("sample1.txt").grand_total(cephalopod_math=True) == 3263827

    print("Tests passed, starting with the puzzle")

    puzzle = TrashCompactor(data.input_file)

    print(puzzle.grand_total(False))
    print(puzzle.grand_total(True))

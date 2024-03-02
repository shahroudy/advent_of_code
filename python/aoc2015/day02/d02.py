import re
from pathlib import Path

from myutils.io_handler import get_input_data


class IWasToldThereWouldBeNoMath:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [sorted(list(map(int, re.findall(r"-?\d+", line)))) for line in lines]

    def total_wrapping_paper(self):
        return sum(n[0] * n[1] * 3 + n[0] * n[2] * 2 + n[1] * n[2] * 2 for n in self.inp)

    def total_ribbon(self):
        return sum((n[0] + n[1]) * 2 + n[0] * n[1] * n[2] for n in self.inp)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = IWasToldThereWouldBeNoMath(filename)
    assert answer1 is None or test.total_wrapping_paper() == answer1
    assert answer2 is None or test.total_ribbon() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 58, 34)
    test_samples("sample2.txt", 43, 14)

    print("Tests passed, starting with the puzzle")

    puzzle = IWasToldThereWouldBeNoMath(data.input_file)
    print(puzzle.total_wrapping_paper())
    print(puzzle.total_ribbon())

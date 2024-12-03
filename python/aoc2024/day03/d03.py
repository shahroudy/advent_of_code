import re
from pathlib import Path

from myutils.io_handler import get_input_data


class MullItOver:
    def __init__(self, filename):
        match_re = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
        self.matches = match_re.findall(Path(filename).read_text())

    def sum_of_all_multiplications(self, consider_switch=False):
        switch = True
        result = 0
        for a, b, do, dont in self.matches:
            if do:
                switch = True
            elif dont:
                switch = False
            elif switch or not consider_switch:
                result += int(a) * int(b)
        return result


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert MullItOver("sample1.txt").sum_of_all_multiplications() == 161
    assert MullItOver("sample2.txt").sum_of_all_multiplications(True) == 48

    print("Tests passed, starting with the puzzle")

    puzzle = MullItOver(data.input_file)

    print(puzzle.sum_of_all_multiplications())
    print(puzzle.sum_of_all_multiplications(True))

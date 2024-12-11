import re
from functools import cache
from pathlib import Path

from myutils.io_handler import get_input_data


class PlutonianPebbles:
    def __init__(self, filename):
        self.inp = [int(n) for n in re.findall(r"\d+", Path(filename).read_text())]

    @cache
    def stones(self, n, steps):
        if steps == 1:
            if n == 0:
                return 1
            elif len(str(n)) % 2 == 0:
                return 2
            else:
                return 1
        else:
            if n == 0:
                return self.stones(1, steps - 1)
            elif len(n_str := str(n)) % 2 == 0:
                n1, n2 = int(n_str[: len(n_str) // 2]), int(n_str[len(n_str) // 2 :])
                return self.stones(n1, steps - 1) + self.stones(n2, steps - 1)
            else:
                return self.stones(n * 2024, steps - 1)

    def stone_count_after(self, times=25):
        return sum(self.stones(n, times) for n in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PlutonianPebbles("sample1.txt").stone_count_after(1) == 3
    assert PlutonianPebbles("sample1.txt").stone_count_after(2) == 4
    assert PlutonianPebbles("sample1.txt").stone_count_after(3) == 5
    assert PlutonianPebbles("sample1.txt").stone_count_after(4) == 9
    assert PlutonianPebbles("sample1.txt").stone_count_after(5) == 13
    assert PlutonianPebbles("sample1.txt").stone_count_after(6) == 22
    assert PlutonianPebbles("sample1.txt").stone_count_after(25) == 55312

    print("Tests passed, starting with the puzzle")

    puzzle = PlutonianPebbles(data.input_file)

    print(puzzle.stone_count_after(25))
    print(puzzle.stone_count_after(75))

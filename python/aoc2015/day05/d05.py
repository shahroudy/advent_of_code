import re
from pathlib import Path

from myutils.io_handler import get_input_data


class DoesntHeHaveInternElvesForThis:
    def __init__(self, filename):
        self.nice_a, self.nice_b = list(), list()
        for s in Path(filename).read_text().splitlines():
            self.nice_a.append(self.is_nice_a(s))
            self.nice_b.append(self.is_nice_b(s))

    def is_nice_a(self, s):
        return bool(
            len(re.findall(r"[aeiou]", s)) >= 3
            and re.search(r"(.)\1", s)
            and not re.search(r"ab|cd|pq|xy", s)
        )

    def is_nice_b(self, s):
        return bool(re.search(r"(..).*\1", s) and re.search(r"(.).\1", s))


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = DoesntHeHaveInternElvesForThis(filename)
    assert answer1 is None or test.nice_a == answer1
    assert answer2 is None or test.nice_b == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", [True, True, False, False, False], None)
    test_samples("sample2.txt", None, [True, True, False, False])

    print("Tests passed, starting with the puzzle")

    puzzle = DoesntHeHaveInternElvesForThis(data.input_file)

    print(sum(puzzle.nice_a))
    print(sum(puzzle.nice_b))

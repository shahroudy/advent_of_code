import re
from functools import cache
from pathlib import Path

from myutils.io_handler import get_input_data


class ExplosivesInCyberspace:
    def __init__(self, filename):
        self.input = Path(filename).read_text()

    @cache
    def get_length(self, version, txt=None):
        txt = self.input if txt is None else txt
        if m := re.search(r"\((\d+)x(\d+)\)", txt):
            ln, rep = map(int, m.groups())
            sub, rest = txt[m.end() : m.end() + ln], txt[m.end() + ln :]
            if version == 1:
                return m.start() + ln * rep + self.get_length(1, rest)
            else:
                return m.start() + rep * self.get_length(2, sub) + self.get_length(2, rest)
        else:
            return len(txt)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ExplosivesInCyberspace(filename)
    assert answer1 is None or test.get_length(version=1) == answer1
    assert answer2 is None or test.get_length(version=2) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 6, None)
    test_samples("sample2.txt", 7, None)
    test_samples("sample3.txt", 9, 9)
    test_samples("sample4.txt", 11, None)
    test_samples("sample5.txt", 6, None)
    test_samples("sample6.txt", 18, 20)
    test_samples("sample7.txt", None, 241920)
    test_samples("sample8.txt", None, 445)

    print("Tests passed, starting with the puzzle")

    puzzle = ExplosivesInCyberspace(data.input_file)

    print(puzzle.get_length(version=1))
    print(puzzle.get_length(version=2))

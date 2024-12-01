import re
from pathlib import Path

from myutils.io_handler import get_input_data


class PasswordPhilosophy:
    def __init__(self, filename):
        self.inp = []
        line_re = re.compile(r"(\d+)-(\d+) (\w): (.*)")
        for line in Path(filename).read_text().splitlines():
            m, M, c, s = line_re.match(line).groups()
            self.inp.append((int(m), int(M), c, s))

    def valid_passwords_count(self):
        return sum(m <= s.count(c) <= M for m, M, c, s in self.inp)

    def valid_passwords_position(self):
        return sum((s[m - 1] == c) ^ (s[M - 1] == c) for m, M, c, s in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PasswordPhilosophy("sample1.txt").valid_passwords_count() == 2
    assert PasswordPhilosophy("sample1.txt").valid_passwords_position() == 1

    print("Tests passed, starting with the puzzle")

    puzzle = PasswordPhilosophy(data.input_file)

    print(puzzle.valid_passwords_count())
    print(puzzle.valid_passwords_position())

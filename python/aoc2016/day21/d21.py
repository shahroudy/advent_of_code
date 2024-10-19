import re
from itertools import permutations
from pathlib import Path

from myutils.io_handler import get_input_data


class ScrambledLettersAndHash:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().splitlines()
        self.REs = [
            re.compile(r"swap position (\d+) with position (\d+)"),
            re.compile(r"swap letter (\w+) with letter (\w+)"),
            re.compile(r"rotate (\w+) (\d+) step.*"),
            re.compile(r"rotate based on position of letter (\w+)"),
            re.compile(r"reverse positions (\d+) through (\d+)"),
            re.compile(r"move position (\d+) to position (\d+)"),
        ]

    def scramble(self, s):
        s = list(s)
        for line in self.lines:
            if m := self.REs[0].match(line):
                x, y = map(int, m.groups())
                s[x], s[y] = s[y], s[x]
            elif m := self.REs[1].match(line):
                x, y = m.groups()
                s = [y if c == x else x if c == y else c for c in s]
            elif m := self.REs[2].match(line):
                lr, n = m.groups()
                n = int(n) * (1 if lr == "left" else -1)
                s = s[n:] + s[:n]
            elif m := self.REs[3].match(line):
                x = m.groups()[0]
                index = s.index(x)
                shift = (1 + index + (1 if index >= 4 else 0)) % len(s)
                s = s[-shift:] + s[:-shift]
            elif m := self.REs[4].match(line):
                x, y = map(int, m.groups())
                s = s[:x] + s[x : y + 1][::-1] + s[y + 1 :]
            elif m := self.REs[5].match(line):
                x, y = map(int, m.groups())
                b = s[x]
                s = s[:x] + s[x + 1 :]
                s = s[:y] + [b] + s[y:]
            else:
                raise Exception(f"Invalid line: {line}")
        return "".join(s)

    def find_unscrambled(self, s):
        for p in permutations(s):
            if self.scramble(p) == s:
                return "".join(p)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ScrambledLettersAndHash("sample1.txt").scramble("abcde") == "decab"

    print("Tests passed, starting with the puzzle")

    puzzle = ScrambledLettersAndHash(data.input_file)

    print(puzzle.scramble("abcdefgh"))
    print(puzzle.find_unscrambled("fbgdceah"))

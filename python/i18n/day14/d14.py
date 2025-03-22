import re
from pathlib import Path

import kanjize


class MetrificationInJapan:
    def __init__(self, filename):
        self.inp = re.findall(r"^(.+) × (.+)$", Path(filename).read_text(), re.MULTILINE)
        self.d = {
            "尺": 1,
            "間": 6,
            "丈": 10,
            "町": 360,
            "里": 12960,
            "毛": 1.0 / 10000.0,
            "厘": 1.0 / 1000.0,
            "分": 1.0 / 100.0,
            "寸": 1.0 / 10.0,
        }

    def get_length(self, input):
        return int(self.d[input[-1]] * kanjize.kanji2number(input[:-1]) * 10.0 / 33.0)

    def calc(self):
        return sum(self.get_length(x) * self.get_length(y) for x, y in self.inp)


if __name__ == "__main__":
    assert MetrificationInJapan("test-input").calc() == 2177741195
    print("Tests passed, starting with the puzzle")
    print(MetrificationInJapan("input").calc())

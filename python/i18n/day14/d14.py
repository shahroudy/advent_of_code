import os
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
        return self.d[input[-1]] * kanjize.kanji2number(input[:-1]) * 10.0 / 33.0

    def calc(self):
        return int(sum(self.get_length(x) * self.get_length(y) for x, y in self.inp))


if __name__ == "__main__":
    assert MetrificationInJapan("test-input.txt").calc() == 2177741195
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(MetrificationInJapan(f"{input_folder}/i18n2025_day14.txt").calc())

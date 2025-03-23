import os
import re
from collections import defaultdict
from datetime import datetime
from itertools import permutations
from pathlib import Path


class NineEleven:
    def __init__(self, filename):
        self.dates = defaultdict(list)
        for line in Path(filename).read_text().splitlines():
            for name in re.findall(r"[a-zA-Z]+", line):
                self.dates[name].append(list(map(int, re.findall(r"\d+", line))))

    def calc(self):
        sus_names = set()
        for name, dates in self.dates.items():
            for format in permutations(["day", "month", "year"]):
                try:
                    sus = False
                    for date in dates:
                        kwargs = dict(zip(format, date))
                        kwargs["year"] += 2000 if kwargs["year"] < 20 else 1900
                        if datetime(**kwargs) == datetime(2001, 9, 11):
                            sus = True
                    if sus:
                        sus_names.add(name)
                        break
                except ValueError:
                    continue
        return " ".join(sorted(sus_names))


if __name__ == "__main__":

    assert NineEleven("test-input.txt").calc() == "Margot Peter"
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(NineEleven(f"{input_folder}/i18n2025_day09.txt").calc())

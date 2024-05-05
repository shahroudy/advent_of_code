import re
from pathlib import Path

from myutils.io_handler import get_input_data


class AuntSue:
    def __init__(self, filename):
        self.sue = {}
        line_re = re.compile(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")
        for line in Path(filename).read_text().splitlines():
            parts = line_re.match(line).groups()
            self.sue[int(parts[0])] = {parts[i]: int(parts[i + 1]) for i in range(1, 6, 2)}

    def find_aunt_sue_1(self):
        for sue, props in self.sue.items():
            if all(
                props[k] == v
                for k, v in [
                    ("children", 3),
                    ("cats", 7),
                    ("samoyeds", 2),
                    ("pomeranians", 3),
                    ("akitas", 0),
                    ("vizslas", 0),
                    ("goldfish", 5),
                    ("trees", 3),
                    ("cars", 2),
                    ("perfumes", 1),
                ]
                if k in props
            ):
                return sue

    def find_aunt_sue_2(self):
        for sue, props in self.sue.items():
            if (
                all(
                    props[k] == v
                    for k, v in [
                        ("children", 3),
                        ("samoyeds", 2),
                        ("akitas", 0),
                        ("vizslas", 0),
                        ("cars", 2),
                        ("perfumes", 1),
                    ]
                    if k in props
                )
                and all(
                    props[k] > v
                    for k, v in [
                        ("cats", 7),
                        ("trees", 3),
                    ]
                    if k in props
                )
                and all(
                    props[k] < v
                    for k, v in [
                        ("pomeranians", 3),
                        ("goldfish", 5),
                    ]
                    if k in props
                )
            ):
                return sue


if __name__ == "__main__":
    data = get_input_data(__file__)
    puzzle = AuntSue(data.input_file)
    print(puzzle.find_aunt_sue_1())
    print(puzzle.find_aunt_sue_2())

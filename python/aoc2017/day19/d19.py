from pathlib import Path

from myutils.io_handler import get_input_data


class ASeriesOfTubes:
    def __init__(self, filename):
        self.read_map(filename)
        self.follow_route()

    def read_map(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.map = dict()
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch

    def follow_route(self):
        for k, v in self.map.items():
            if k[1] == 0 and v == "|":
                x, y = k
                break
        self.seen_letters, self.steps = "", 0
        direction = (0, 1)
        while True:
            if not (x, y) in self.map:
                break
            ch = self.map[x, y]
            if ch == " ":
                break
            elif ch == "+":
                if direction[1]:  # turn left or right
                    for dx in (-1, 1):
                        if (x + dx, y) in self.map and self.map[x + dx, y] not in " |":
                            direction = (dx, 0)
                else:  # turn up or down
                    for dy in (-1, 1):
                        if (x, y + dy) in self.map and self.map[x, y + dy] not in " -":
                            direction = (0, dy)
            elif ch.isalpha():
                self.seen_letters += ch
            x, y = x + direction[0], y + direction[1]
            self.steps += 1


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = ASeriesOfTubes("sample1.txt")
    assert test.seen_letters == "ABCDEF"
    assert test.steps == 38

    print("Tests passed, starting with the puzzle")

    puzzle = ASeriesOfTubes(data.input_file)

    print(puzzle.seen_letters)
    print(puzzle.steps)

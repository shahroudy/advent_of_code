from pathlib import Path

from myutils.io_handler import get_input_data


class LikeARogue:
    def __init__(self, filename):
        self.inp = Path(filename).read_text().strip()

    def is_safe(self, p):
        return "^" if p in {"^^.", ".^^", "^..", "..^"} else "."

    def new_row(self, row):
        length = len(self.inp)
        row = "." + row + "."
        return "".join([self.is_safe(row[i - 1 : i + 2]) for i in range(1, length + 1)])

    def safe_count(self, rows=10):
        row = self.inp
        count = sum([c == "." for c in row])
        for _ in range(rows - 1):
            row = self.new_row(row)
            count += sum([c == "." for c in row])
        return count


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert LikeARogue("sample1.txt").safe_count(3) == 6
    assert LikeARogue("sample2.txt").safe_count(10) == 38

    print("Tests passed, starting with the puzzle")

    puzzle = LikeARogue(data.input_file)

    print(puzzle.safe_count(40))
    print(puzzle.safe_count(400000))

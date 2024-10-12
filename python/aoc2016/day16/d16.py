from pathlib import Path

from myutils.io_handler import get_input_data


class Puzzle:
    def __init__(self, filename):
        self.inp = [int(c) for c in Path(filename).read_text().strip()]

    def checksum(self, disk_len=20):
        code = self.inp
        while len(code) < disk_len:
            code += [0] + [0 if c else 1 for c in code][::-1]
        code = code[:disk_len]
        while len(code) % 2 == 0:
            code = ["1" if code[i] == code[i + 1] else "0" for i in range(0, len(code) - 1, 2)]
        return "".join(code)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Puzzle("sample1.txt").checksum() == "01100"

    print("Tests passed, starting with the puzzle")

    puzzle = Puzzle(data.input_file)

    print(puzzle.checksum(disk_len=272))
    print(puzzle.checksum(disk_len=35651584))

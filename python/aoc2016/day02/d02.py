from pathlib import Path

from myutils.io_handler import get_input_data


class BathroomSecurity:
    def __init__(self, filename):
        self.moves = Path(filename).read_text().strip().split("\n")

    def load_keypad(self, keypad_file):
        return {
            (col, row): code
            for row, line in enumerate(Path(keypad_file).read_text().split("\n"))
            for col, code in enumerate(line)
            if code != " "
        }

    def key_in(self, keypad_file):
        keypad = self.load_keypad(keypad_file)
        for current, code in keypad.items():
            if code == "5":
                break
        res = ""
        direction = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
        for line in self.moves:
            for move in line:
                next = tuple(current[i] + direction[move][i] for i in range(2))
                current = next if next in keypad else current
            res += keypad[current]
        return res


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = BathroomSecurity(filename)
    assert answer1 is None or test.key_in("keypad1.txt") == answer1
    assert answer2 is None or test.key_in("keypad2.txt") == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", "1985", "5DB3")

    print("Tests passed, starting with the puzzle")

    puzzle = BathroomSecurity(data.input_file)
    print(puzzle.key_in("keypad1.txt"))
    print(puzzle.key_in("keypad2.txt"))

from pathlib import Path

from myutils.io_handler import get_input_data


class SecretEntrance:
    def __init__(self, filename):
        self.inp = [
            (1 if t[0] == "R" else -1, int(t[1:])) for t in Path(filename).read_text().splitlines()
        ]

    def count_zero_ends(self):
        dial = 50
        zero_counts = 0
        for sign, number in self.inp:
            dial = (dial + sign * number) % 100
            if dial == 0:
                zero_counts += 1
        return zero_counts

    def count_zero_passes(self):
        dial = 50
        zero_count = 0
        for sign, number in self.inp:
            for _ in range(number):
                dial = (dial + sign) % 100
                if dial == 0:
                    zero_count += 1
        return zero_count


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SecretEntrance("sample1.txt").count_zero_ends() == 3
    assert SecretEntrance("sample1.txt").count_zero_passes() == 6

    print("Tests passed, starting with the puzzle")

    puzzle = SecretEntrance(data.input_file)

    print(puzzle.count_zero_ends())
    print(puzzle.count_zero_passes())

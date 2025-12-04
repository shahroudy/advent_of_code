from pathlib import Path

from myutils.io_handler import get_input_data


class SecretEntrance:
    def __init__(self, filename):
        text = Path(filename).read_text()
        self.inp = [(1 if t[0] == "R" else -1, int(t[1:])) for t in text.splitlines()]

    def count_zero_ends(self):
        dial, zero_counts = 50, 0
        for sign, clicks in self.inp:
            dial = (dial + sign * clicks) % 100
            zero_counts += dial == 0
        return zero_counts

    def count_zero_passes(self):
        dial, zero_counts = 50, 0
        for sign, clicks in self.inp:
            clicks_till_zero = (sign * (100 - dial)) % 100
            if clicks >= clicks_till_zero:
                remaining_clicks = clicks - clicks_till_zero
                zero_counts += remaining_clicks // 100 + (clicks_till_zero > 0)
                dial = sign * remaining_clicks % 100
            else:
                dial += sign * clicks
        return zero_counts


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SecretEntrance("sample1.txt").count_zero_ends() == 3
    assert SecretEntrance("sample1.txt").count_zero_passes() == 6

    print("Tests passed, starting with the puzzle")

    puzzle = SecretEntrance(data.input_file)

    print(puzzle.count_zero_ends())
    print(puzzle.count_zero_passes())

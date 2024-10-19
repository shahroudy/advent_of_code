from pathlib import Path

from myutils.exrange import ExRange
from myutils.io_handler import get_input_data


class FirewallRules:
    def __init__(self, filename, max_ip=9):
        values = [list(map(int, r.split("-"))) for r in Path(filename).read_text().splitlines()]
        invalid_ranges = ExRange([range(v[0], v[1] + 1) for v in values])
        valid_ranges = ExRange(0, max_ip + 1) - invalid_ranges
        self.first_valid = valid_ranges.ranges[0].start if valid_ranges.ranges else None
        self.valid_count = valid_ranges.length()


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert FirewallRules("sample1.txt").first_valid == 3

    print("Tests passed, starting with the puzzle")

    puzzle = FirewallRules(data.input_file, max_ip=4294967295)

    print(puzzle.first_valid)
    print(puzzle.valid_count)

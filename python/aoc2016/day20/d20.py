from pathlib import Path

from myutils.io_handler import get_input_data


class FirewallRules:
    def __init__(self, filename, max_ip=9):
        values = [list(map(int, r.split("-"))) for r in Path(filename).read_text().splitlines()]
        invalid_ranges = [range(v[0], v[1] + 1) for v in values]
        self.valid_count = 0
        self.first_valid = None
        ip = 0
        while ip <= max_ip:
            for r in invalid_ranges:
                if ip in r:
                    ip = r.stop
                    break
            else:
                if self.first_valid is None:
                    self.first_valid = ip
                next_invalid = max_ip + 1
                for r in invalid_ranges:
                    if ip < r.start < next_invalid:
                        next_invalid = r.start
                self.valid_count += next_invalid - ip
                ip = next_invalid


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert FirewallRules("sample1.txt").first_valid == 3

    print("Tests passed, starting with the puzzle")

    puzzle = FirewallRules(data.input_file, max_ip=4294967295)

    print(puzzle.first_valid)
    print(puzzle.valid_count)

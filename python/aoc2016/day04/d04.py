import re
from collections import Counter
from pathlib import Path

from myutils.io_handler import get_input_data


class SecurityThroughObscurity:
    def __init__(self, filename):
        self.inp = []
        line_re = re.compile(r"(.*)-(\d+)\[(\w+)\]")
        for line in Path(filename).read_text().splitlines():
            parts = line_re.match(line).groups()
            self.inp.append((parts[0], int(parts[1]), parts[2]))

    def sum_of_real_sector_ids(self):
        sector_sum = 0
        for name, sector, checksum in self.inp:
            counts = Counter(name.replace("-", ""))
            top_chars = sorted(counts.keys(), key=lambda x: (-counts[x], x))
            if "".join(top_chars[:5]) == checksum:
                sector_sum += sector
        return sector_sum

    def decrypt(self, name, sector):
        mapping = {
            chr(c): chr((c - ord("a") + sector) % 26 + ord("a"))
            for c in range(ord("a"), ord("z") + 1)
        }
        mapping["-"] = " "
        return "".join(mapping[c] for c in name)

    def sector_id_of_northpole_storage(self):
        for name, sector, _ in self.inp:
            if self.decrypt(name, sector) == "northpole object storage":
                return sector


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = SecurityThroughObscurity("sample1.txt")
    assert test.sum_of_real_sector_ids() == 1514
    assert test.decrypt("qzmt-zixmtkozy-ivhz", 343) == "very encrypted name"

    print("Tests passed, starting with the puzzle")

    puzzle = SecurityThroughObscurity(data.input_file)

    print(puzzle.sum_of_real_sector_ids())
    print(puzzle.sector_id_of_northpole_storage())

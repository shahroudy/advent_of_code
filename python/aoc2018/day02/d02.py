from collections import Counter
from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class InventoryManagementSystem:
    def __init__(self, filename):
        self.box_ids = Path(filename).read_text().splitlines()

    def checksum(self):
        count_2, count_3 = 0, 0
        for id in self.box_ids:
            counts = Counter(id)
            count_2 += 2 in counts.values()
            count_3 += 3 in counts.values()
        return count_2 * count_3

    def common_letters(self):
        for id1, id2 in combinations(self.box_ids, 2):
            common = [c1 for (c1, c2) in zip(id1, id2) if c1 == c2]
            if len(common) == len(id1) - 1:
                return "".join(common)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert InventoryManagementSystem("sample1.txt").checksum() == 12
    assert InventoryManagementSystem("sample2.txt").common_letters() == "fgij"

    print("Tests passed, starting with the puzzle")

    puzzle = InventoryManagementSystem(data.input_file)

    print(puzzle.checksum())
    print(puzzle.common_letters())

from itertools import count
from pathlib import Path

from myutils.exrange import ExRange
from myutils.io_handler import get_input_data


class GiftShop:
    def __init__(self, filename):
        text = Path(filename).read_text()
        range_limits = [[int(n) for n in rng.split("-")] for rng in text.split(",")]
        self.ranges = ExRange([range(start, end + 1) for start, end in range_limits])
        self.max_id_digits = max(len(str(end)) for _, end in range_limits)

    def sum_of_invalid_ids(self, only_twice=False):
        invalid_ids = set()
        for repeats in range(2, 3 if only_twice else self.max_id_digits + 1):
            for i in count(1):
                invalid_str = str(i) * repeats
                if len(invalid_str) > self.max_id_digits:
                    break
                if (invalid_id := int(invalid_str)) in self.ranges:
                    invalid_ids.add(invalid_id)
        return sum(invalid_ids)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert GiftShop("sample1.txt").sum_of_invalid_ids(only_twice=True) == 1227775554
    assert GiftShop("sample1.txt").sum_of_invalid_ids(only_twice=False) == 4174379265

    print("Tests passed, starting with the puzzle")

    puzzle = GiftShop(data.input_file)

    print(puzzle.sum_of_invalid_ids(only_twice=True))
    print(puzzle.sum_of_invalid_ids(only_twice=False))

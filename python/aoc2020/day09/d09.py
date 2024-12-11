from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class EncodingError:
    def __init__(self, filename, preamble_size=25):
        self.inp = [int(n) for n in Path(filename).read_text().splitlines()]
        self.preamble_size = preamble_size
        self.first_invalid = self.find_first_invalid()

    def find_first_invalid(self):
        for i in range(self.preamble_size, len(self.inp)):
            for a, b in combinations(self.inp[i - self.preamble_size : i], 2):
                if a + b == self.inp[i]:
                    break
            else:
                return self.inp[i]

    def encryption_weakness(self):
        sum_lookup = dict()
        sum = 0
        integral = {-1: sum}
        for i, n in enumerate(self.inp):
            sum += n
            integral[i] = sum
            sum_lookup[sum] = i
        for i in range(len(self.inp)):
            if j := sum_lookup.get(integral[i - 1] + self.first_invalid, None):
                nums = self.inp[i : j + 1]
                return min(nums) + max(nums)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = EncodingError("sample1.txt", 5)
    assert test.first_invalid == 127
    assert test.encryption_weakness() == 62

    print("Tests passed, starting with the puzzle")

    puzzle = EncodingError(data.input_file)

    print(puzzle.first_invalid)
    print(puzzle.encryption_weakness())

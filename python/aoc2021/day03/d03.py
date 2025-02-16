from functools import reduce
from pathlib import Path

from myutils.io_handler import get_input_data


class BinaryDiagnostic:
    def __init__(self, filename):
        self.inp = Path(filename).read_text().splitlines()
        self.code_len = len(self.inp[0])

    def power_consumption(self):
        half = len(self.inp) // 2
        most_common = [int(sum(n[i] == "1" for n in self.inp) > half) for i in range(self.code_len)]
        oxygen_generator_rating = reduce(lambda x, y: 2 * x + y, most_common)
        co2_scrubber_rating = 2**self.code_len - 1 - oxygen_generator_rating
        return oxygen_generator_rating * co2_scrubber_rating

    def filter_out(self, most_common):
        nums = self.inp.copy()
        for i in range(self.code_len):
            oc, zc = sum(n[i] == "1" for n in nums), sum(n[i] == "0" for n in nums)
            bit = "1" if (oc < zc) ^ most_common else "0"
            nums = [n for n in nums if n[i] == bit]
            if len(nums) == 1:
                return int(nums[0], 2)

    def life_support_rating(self):
        return self.filter_out(True) * self.filter_out(False)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert BinaryDiagnostic("sample1.txt").power_consumption() == 198
    assert BinaryDiagnostic("sample1.txt").life_support_rating() == 230

    print("Tests passed, starting with the puzzle")

    puzzle = BinaryDiagnostic(data.input_file)

    print(puzzle.power_consumption())
    print(puzzle.life_support_rating())

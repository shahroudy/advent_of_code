import os
from pathlib import Path
from functools import cache
from myutils.io_handler import get_input_data


class FullOfHotAir:
    def __init__(self, filename):
        self.snafu_nums = Path(filename).read_text().strip().split("\n")
        self.max_digits = 10 + max([len(line) for line in self.snafu_nums])
        self.digit_values = {"1": 1, "2": 2, "=": -2, "-": -1, "0": 0}

    @cache
    def snafu_to_int(self, s):
        if s:
            return self.digit_values[s[-1]] + 5 * self.snafu_to_int(s[:-1])
        return 0

    def int_to_snafu(self, n):
        snafu = ""
        for rank in range(self.max_digits, -1, -1):
            min_remainder = float("inf")
            for digit, digit_value in self.digit_values.items():
                ranked_value = digit_value * 5**rank
                remainder = abs(n - ranked_value)
                if remainder < min_remainder:
                    min_remainder = remainder
                    best_digit = digit
                    best_remainder = n - ranked_value
            n = best_remainder
            snafu = snafu + best_digit
            if snafu == "0":
                snafu = ""
        return snafu

    def sum_of_snafu_numbers(self):
        return self.int_to_snafu(sum([self.snafu_to_int(snafu) for snafu in self.snafu_nums]))


def test_samples(filename, answer):
    test = FullOfHotAir(filename)
    assert test.sum_of_snafu_numbers() == answer


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", "2=-1=0")
    full_of_hot_air = FullOfHotAir(data.input_file)
    print(full_of_hot_air.sum_of_snafu_numbers())

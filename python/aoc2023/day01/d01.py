import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class Trebuchet:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")

    def sum_of_first_and_last_digits(self):
        result = 0
        for line in self.lines:
            first_match = re.search(r"\d", line).group()
            last_match = re.search(r"\d", line[::-1]).group()
            result += int(first_match + last_match)
        return result

    def sum_of_first_and_last_alphanumeric_digits(self):
        alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        vals = {s: i for i, s in enumerate(alpha)} | {str(i): i for i in range(10)}
        digits_re = "|".join(vals.keys())
        result = 0
        for line in self.lines:
            first_match = vals[re.search(digits_re, line).group()]
            last_match = vals[re.search(digits_re[::-1], line[::-1]).group()[::-1]]
            result += first_match * 10 + last_match
        return result


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Trebuchet(filename)
    assert answer1 is None or test.sum_of_first_and_last_digits() == answer1
    assert answer2 is None or test.sum_of_first_and_last_alphanumeric_digits() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 142, None)
    test_samples("sample2.txt", None, 281)

    print("Tests passed, starting with the puzzle")

    puzzle = Trebuchet(data.input_file)
    print(puzzle.sum_of_first_and_last_digits())
    print(puzzle.sum_of_first_and_last_alphanumeric_digits())

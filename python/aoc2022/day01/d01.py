import os
from pathlib import Path
from myutils.io_handler import get_input_data


class CalorieCounting:
    def __init__(self, filename):
        input = Path(filename).read_text().strip()
        elves = [[int(c) for c in elf.split("\n")] for elf in input.split("\n\n")]
        self.calories = [sum(elf) for elf in elves]
        self.calories.sort(reverse=True)

    def max_cal_elf(self):
        return self.calories[0]

    def max_cal_three_elves(self):
        return sum(self.calories[:3])


def test_samples(filename, answer1, answer2):
    test = CalorieCounting(filename)
    assert test.max_cal_elf() == answer1
    assert test.max_cal_three_elves() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 24000, 45000)

    calorie_counting = CalorieCounting(data.input_file)
    print(calorie_counting.max_cal_elf())
    print(calorie_counting.max_cal_three_elves())

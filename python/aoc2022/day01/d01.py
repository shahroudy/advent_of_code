import os
from pathlib import Path


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
    test_samples("sample1.txt", 24000, 45000)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day01.txt'
    calorie_counting = CalorieCounting(input_file)
    print(calorie_counting.max_cal_elf())
    print(calorie_counting.max_cal_three_elves())

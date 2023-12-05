import os
from myutils.file_reader import read_int_list


class ChronalCalibration:
    def __init__(self, filename):
        self.nums = read_int_list(filename)

    def resulting_frequency(self):
        return sum(self.nums)

    def first_twice_frequency(self):
        sum = 0
        freqs = set()
        while True:
            for n in self.nums:
                sum += n
                if sum in freqs:
                    return sum
                else:
                    freqs.add(sum)


if __name__ == "__main__":

    test1 = ChronalCalibration("test1.txt")
    assert test1.resulting_frequency() == 3
    assert test1.first_twice_frequency() == 2

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day01.txt'
    chronal_calibration = ChronalCalibration(input_file)
    print(chronal_calibration.resulting_frequency())
    print(chronal_calibration.first_twice_frequency())

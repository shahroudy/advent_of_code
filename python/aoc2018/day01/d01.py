import os
from myutils.file_reader import read_int_list
from myutils.io_handler import get_input_data


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
    data = get_input_data(__file__)

    test1 = ChronalCalibration("test1.txt")
    assert test1.resulting_frequency() == 3
    assert test1.first_twice_frequency() == 2

    chronal_calibration = ChronalCalibration(data.input_file)
    print(chronal_calibration.resulting_frequency())
    print(chronal_calibration.first_twice_frequency())

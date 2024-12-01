import os
from myutils.file_reader import read_int_list
from myutils.io_handler import get_input_data


class SonarSweep:
    def __init__(self, filename):
        self.nums = read_int_list(filename)

    def depth_increments(self):
        return sum([self.nums[i + 1] > self.nums[i] for i in range(len(self.nums) - 1)])

    def depth_windows_increments(self):
        return sum(
            [
                sum(self.nums[i + 1 : i + 4]) > sum(self.nums[i : i + 3])
                for i in range(len(self.nums) - 3)
            ]
        )


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = SonarSweep("test1.txt")
    assert test1.depth_increments() == 7
    assert test1.depth_windows_increments() == 5

    sonar_sweep = SonarSweep(data.input_file)
    print(
        sonar_sweep.depth_increments(),
        sonar_sweep.depth_windows_increments(),
    )

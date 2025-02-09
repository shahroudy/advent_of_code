import os
from collections import defaultdict
from myutils.file_reader import read_int_list
from myutils.io_handler import get_input_data


class Lanternfish:
    def __init__(self, filename):
        self.nums = list(map(int, read_int_list(filename)))

    def simulate(self, steps):
        count = defaultdict(int)
        for n in self.nums:
            count[n] += 1
        for _ in range(steps):
            zeros = count[0]
            for v in range(8):
                count[v] = count[v + 1]
            count[8] = zeros
            count[6] += zeros
        return sum(count.values())


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = Lanternfish("test1.txt")
    assert test1.simulate(18) == 26
    assert test1.simulate(80) == 5934
    assert test1.simulate(256) == 26984457539

    lanternfish = Lanternfish(data.input_file)
    print(lanternfish.simulate(80))
    print(lanternfish.simulate(256))

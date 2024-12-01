import os
from myutils.file_reader import read_int_list
from myutils.io_handler import get_input_data


class TheTreacheryOfWhales:
    def __init__(self, filename):
        self.nums = read_int_list(filename)
        self.process_fuel_needed()

    def simple_align(self):
        min_fuel = -1
        for i in self.nums:
            fuel = 0
            for j in self.nums:
                fuel += abs(i - j)
            min_fuel = min(min_fuel, fuel) if min_fuel >= 0 else fuel
        return min_fuel

    def process_fuel_needed(self):
        self.dist_fuel = dict()
        max_dist = max(self.nums) - min(self.nums)
        acc = 0
        for i in range(max_dist + 1):
            acc += i
            self.dist_fuel[i] = acc

    def full_align(self):
        min_fuel = -1
        for i in range(max(self.nums)):
            fuel = 0
            for j in self.nums:
                fuel += self.dist_fuel[abs(i - j)]
                if 0 <= min_fuel < fuel:
                    break
            min_fuel = min(min_fuel, fuel) if min_fuel >= 0 else fuel
        return min_fuel


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = TheTreacheryOfWhales("test1.txt")
    assert test1.simple_align() == 37
    assert test1.full_align() == 168

    treachery = TheTreacheryOfWhales(data.input_file)
    print(treachery.simple_align())
    print(treachery.full_align())

import os
from collections import Counter
from myutils.file_reader import read_lines


class InventoryManagementSystem:
    def __init__(self, filename):
        self.lines = read_lines(filename)

    def checksum(self):
        two_counter = three_counter = 0
        for line in self.lines:
            has_two = False
            has_three = False
            counter = Counter(line)
            for counter_values in counter.values():
                if counter_values == 2:
                    has_two = True
                if counter_values == 3:
                    has_three = True
                if has_two and has_three:
                    break
            two_counter += has_two
            three_counter += has_three
        return two_counter * three_counter

    def common_in_box_ids(self):
        for line1 in self.lines:
            for line2 in self.lines:
                if line1 == line2:
                    continue
                diff = 0
                common_code = []
                for head in range(len(line1)):
                    if line1[head] == line2[head]:
                        common_code.append(line1[head])
                    else:
                        diff += 1
                    if diff > 1:
                        continue
                if diff == 1:
                    return "".join(common_code)


if __name__ == "__main__":

    test1 = InventoryManagementSystem("test1.txt")
    assert test1.common_in_box_ids() == "fgij"

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day02.txt'
    ims = InventoryManagementSystem(input_file)
    print(ims.checksum())
    print(ims.common_in_box_ids())

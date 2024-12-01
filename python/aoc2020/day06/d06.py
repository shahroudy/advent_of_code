import os
from functools import reduce
from myutils.file_reader import read_line_groups
from myutils.io_handler import get_input_data


class CustomList:
    def __init__(self, filename):
        self.custom_sets = read_line_groups(filename)

    def calc_anyone(self):
        return sum(
            [
                len(reduce(lambda x, y: set(x) | set(y), custom_set))
                for custom_set in self.custom_sets
            ]
        )

    def calc_everyone(self):
        return sum(
            [
                len(reduce(lambda x, y: set(x) & set(y), custom_set))
                for custom_set in self.custom_sets
            ]
        )


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_custom_list = CustomList("test.txt")
    assert test_custom_list.calc_anyone() == 11
    assert test_custom_list.calc_everyone() == 6

    custom_list = CustomList(data.input_file)
    print(custom_list.calc_anyone(), custom_list.calc_everyone())

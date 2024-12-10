import re
from collections import defaultdict
from functools import cache
from pathlib import Path

from myutils.io_handler import get_input_data


class HandyHaversacks:
    def __init__(self, filename):
        left_re = re.compile(r"(\w+ \w+) bags contain")
        right_re = re.compile(r"(\d+) (\w+ \w+) bag")
        self.includes = defaultdict(dict)
        self.included = defaultdict(set)
        for line in Path(filename).read_text().splitlines():
            container_bag_name = left_re.match(line).group(1)
            for number, bag_name in right_re.findall(line):
                self.includes[container_bag_name][bag_name] = int(number)
                self.included[bag_name].add(container_bag_name)

    @cache
    def contained(self, bag):
        result = set()
        for b in self.included[bag]:
            result.add(b)
            result |= self.contained(b)
        return result

    def bag_colors_containing_shiny_gold(self):
        return len(self.contained("shiny gold"))

    @cache
    def contains(self, bag):
        return 1 + sum(number * self.contains(bag) for bag, number in self.includes[bag].items())

    def number_of_bags_inside_a_shiny_gold(self):
        return self.contains("shiny gold") - 1


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert HandyHaversacks("sample1.txt").bag_colors_containing_shiny_gold() == 4
    assert HandyHaversacks("sample1.txt").number_of_bags_inside_a_shiny_gold() == 32
    assert HandyHaversacks("sample2.txt").number_of_bags_inside_a_shiny_gold() == 126

    print("Tests passed, starting with the puzzle")

    puzzle = HandyHaversacks(data.input_file)

    print(puzzle.bag_colors_containing_shiny_gold())
    print(puzzle.number_of_bags_inside_a_shiny_gold())

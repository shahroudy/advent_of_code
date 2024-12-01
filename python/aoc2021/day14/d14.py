import os
from collections import defaultdict
from myutils.file_reader import read_line_groups


class ExtendedPolymerization:
    def __init__(self, filename):
        self.lg = read_line_groups(filename)
        self.process()

    def process(self):
        self.polymer_template = self.lg[0][0]
        self.reactions = dict()
        for line in self.lg[1]:
            left, _, right = line.split()
            self.reactions[left] = right

    def simulate_polymerization(self, steps):
        # count the elements and polymers
        counter = defaultdict(int)
        for i in range(len(self.polymer_template) - 1):
            counter[self.polymer_template[i : i + 2]] += 1
            counter[self.polymer_template[i]] += 1
        counter[self.polymer_template[-1]] += 1

        for _ in range(steps):
            # update the counts based on reactions
            new_counter = counter.copy()
            for left, right in self.reactions.items():
                new_counter[left[0] + right] += counter[left]
                new_counter[right + left[1]] += counter[left]
                new_counter[right] += counter[left]
                new_counter[left] -= counter[left]
            counter = new_counter

        element_counts = [count for (polymer, count) in counter.items() if len(polymer) == 1]
        return max(element_counts) - min(element_counts)


if __name__ == "__main__":

    test1 = ExtendedPolymerization("test1.txt")
    assert test1.simulate_polymerization(steps=10) == 1588
    assert test1.simulate_polymerization(steps=40) == 2188189693529

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day14.txt'
    extended_polymerization = ExtendedPolymerization(input_file)
    print(extended_polymerization.simulate_polymerization(steps=10))
    print(extended_polymerization.simulate_polymerization(steps=40))

from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class ExtendedPolymerization:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.polymer = lines[0]
        self.rules = {a: b for a, b in [line.split(" -> ") for line in lines[2:]]}

    def reset_pairs(self):
        self.pairs = defaultdict(int)
        for left, right in zip(self.polymer, self.polymer[1:]):
            self.pairs[left + right] += 1

    def polymerize(self):
        new_pairs = defaultdict(int)
        for pair, quantity in self.pairs.items():
            if pair in self.rules:
                inserted_element = self.rules[pair]
                left, right = pair
                new_pairs[left + inserted_element] += quantity
                new_pairs[inserted_element + right] += quantity
            else:
                new_pairs[pair] += quantity
        self.pairs = new_pairs

    def get_element_counts(self):
        double_counts = defaultdict(int)
        double_counts[self.polymer[0]] = double_counts[self.polymer[-1]] = 1
        for (left, right), quantity in self.pairs.items():
            double_counts[left] += quantity
            double_counts[right] += quantity
        return {element: count // 2 for element, count in double_counts.items()}

    def quantity_difference_between_most_and_least_common(self, steps=40):
        self.reset_pairs()
        for _ in range(steps):
            self.polymerize()
        counts = self.get_element_counts().values()
        return max(counts) - min(counts)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = ExtendedPolymerization("sample1.txt")
    assert test.quantity_difference_between_most_and_least_common(steps=0) == 1
    assert test.quantity_difference_between_most_and_least_common(steps=1) == 1
    assert test.quantity_difference_between_most_and_least_common(steps=10) == 1588
    assert test.quantity_difference_between_most_and_least_common(steps=40) == 2188189693529

    print("Tests passed, starting with the puzzle")

    puzzle = ExtendedPolymerization(data.input_file)

    print(puzzle.quantity_difference_between_most_and_least_common(steps=10))
    print(puzzle.quantity_difference_between_most_and_least_common(steps=40))

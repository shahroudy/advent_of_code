import os
from pathlib import Path


class AlchemicalReduction:
    def __init__(self, filename):
        self.input = Path(filename).read_text().strip()

    def size_after_reaction(self, removed_polymer=None):
        stack = []
        for polymer in self.input:
            if polymer.upper() == removed_polymer:
                continue
            if stack and stack[-1].upper() == polymer.upper() and stack[-1] != polymer:
                stack.pop()
            else:
                stack.append(polymer)
        return len(stack)

    def min_size_after_elimination(self):
        return min(self.size_after_reaction(removed_polymer=p) for p in set(self.input.upper()))


if __name__ == "__main__":

    test1 = AlchemicalReduction("test1.txt")
    assert test1.size_after_reaction() == 10
    assert test1.min_size_after_elimination() == 4

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2018_day05.txt'
    alchemical_reduction = AlchemicalReduction(input_file)
    print(alchemical_reduction.size_after_reaction())
    print(alchemical_reduction.min_size_after_elimination())

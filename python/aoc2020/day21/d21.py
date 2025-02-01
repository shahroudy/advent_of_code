import re
from functools import reduce
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.matching import find_match_dict


class AllergenAssessment:
    def __init__(self, filename):
        inputs = re.findall(r"^(.+) \(contains (.+)\)$", Path(filename).read_text(), re.MULTILINE)
        self.input = [(set(left.split()), set(right.split(", "))) for left, right in inputs]
        self.allergens = reduce(set.union, [a for _, a in self.input])
        self.ingredients = reduce(set.union, [i for i, _ in self.input])
        connections = {
            allergen: reduce(set.intersection, [i for i, a in self.input if allergen in a])
            for allergen in self.allergens
        }
        self.match = find_match_dict(connections)

    def no_allergen_ingredient_count(self):
        matched_ingredients = set(self.match.values())
        return sum(len(set(i) - matched_ingredients) for i, _ in self.input)

    def canonical_dangerous_ingredient_list(self):
        return ",".join([self.match[a] for a in sorted(self.allergens)])


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = AllergenAssessment("sample1.txt")
    assert test.no_allergen_ingredient_count() == 5
    assert test.canonical_dangerous_ingredient_list() == "mxmxvkd,sqjhc,fvjkl"

    print("Tests passed, starting with the puzzle")

    puzzle = AllergenAssessment(data.input_file)

    print(puzzle.no_allergen_ingredient_count())
    print(puzzle.canonical_dangerous_ingredient_list())

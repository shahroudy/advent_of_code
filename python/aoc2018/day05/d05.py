from pathlib import Path

from myutils.io_handler import get_input_data


class AlchemicalReduction:
    def __init__(self, filename):
        self.polymer = Path(filename).read_text().strip()

    def reacts(self, a, b):
        return a != b and a.lower() == b.lower()

    def size_after_reactions(self, remove=None):
        result = []
        for unit in [p for p in self.polymer if p.lower() != remove]:
            if result and self.reacts(result[-1], unit):
                result.pop()
            else:
                result.append(unit)
        return len(result)

    def shortest_possible_polymer(self):
        all_units = set(self.polymer.lower())
        return min(self.size_after_reactions(remove=unit) for unit in all_units)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert AlchemicalReduction("sample1.txt").size_after_reactions() == 10
    assert AlchemicalReduction("sample1.txt").shortest_possible_polymer() == 4

    print("Tests passed, starting with the puzzle")

    puzzle = AlchemicalReduction(data.input_file)

    print(puzzle.size_after_reactions())
    print(puzzle.shortest_possible_polymer())

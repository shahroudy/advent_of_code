import re
from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class FourDimensionalAdventure:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.inp = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def constellations(self):
        connected = defaultdict(set)
        for p in range(len(self.inp)):
            for q in range(p + 1, len(self.inp)):
                if sum(abs(a - b) for a, b in zip(self.inp[p], self.inp[q])) <= 3:
                    connected[p].add(q)
                    connected[q].add(p)
        not_visited = set(range(len(self.inp)))
        cc = 0
        while not_visited:
            to_visit = {not_visited.pop()}
            visited = to_visit.copy()
            while to_visit:
                p = to_visit.pop()
                not_visited.discard(p)
                to_visit.update(connected[p] - visited)
                visited.update(connected[p])
            cc += 1
        return cc


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert FourDimensionalAdventure("sample1.txt").constellations() == 2
    assert FourDimensionalAdventure("sample2.txt").constellations() == 4
    assert FourDimensionalAdventure("sample3.txt").constellations() == 3
    assert FourDimensionalAdventure("sample4.txt").constellations() == 8
    assert FourDimensionalAdventure("sample5.txt").constellations() == 1

    print("Tests passed, starting with the puzzle")

    puzzle = FourDimensionalAdventure(data.input_file)

    print(puzzle.constellations())

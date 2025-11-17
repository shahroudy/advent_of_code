from collections import namedtuple
from itertools import product
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.search import Search_Dijkstra
from myutils.utils import read_map_of_digits


class MapSearch(Search_Dijkstra):
    State = namedtuple("state", ["point", "cost"])

    def get_next_states(self, state):
        point, cost = state
        for n in point.n4():
            if n in self.nodes:
                yield self.State(n, cost + self.nodes[n])

    def cost(self, state):
        return state.cost

    def state_core(self, state):
        return state.point


class Chiton:
    def __init__(self, filename):
        self.inp, self.rows, self.cols = read_map_of_digits(Path(filename).read_text())

    def lowest_total_risk(self, extend_map=False):
        risk_map = self.inp if not extend_map else self.get_extended_map()
        search = MapSearch(initial_state=MapSearch.State(Point(0, 0), 0), nodes=risk_map)
        shortest, _ = search.search()
        return shortest[max(shortest.keys())]

    def get_extended_map(self):
        return {
            Point(point.x + i * self.cols, point.y + j * self.rows): ((i + j + risk) - 1) % 9 + 1
            for point, risk in self.inp.items()
            for i, j in product(range(0, 5), repeat=2)
        }


if __name__ == "__main__":
    data = get_input_data(__file__)

    # region Tests
    test = Chiton("sample1.txt")
    assert test.lowest_total_risk(extend_map=False) == 40
    assert test.lowest_total_risk(extend_map=True) == 315

    print("Tests passed, starting with the puzzle")

    puzzle = Chiton(data.input_file)

    print(puzzle.lowest_total_risk(extend_map=False))
    print(puzzle.lowest_total_risk(extend_map=True))

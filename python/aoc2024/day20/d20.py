from collections import namedtuple
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.search import Search_Dijkstra


class MapSearch(Search_Dijkstra):
    State = namedtuple("state", ["point", "steps", "cost"])

    def get_next_states(self, state):
        point, steps, cost = state
        for n in point.n4():
            if n in self.nodes:
                yield self.State(n, steps + 1, cost + 1)

    def cost(self, state):
        return state.cost

    def state_core(self, state):
        return state.point


class RaceCondition:
    def __init__(self, filename):
        self.track = set()
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                if ch in ".SE":
                    self.track.add(Point(col, row))
                if ch == "S":
                    self.start = Point(col, row)
                if ch == "E":
                    self.goal = Point(col, row)
        self.dist, _ = MapSearch(nodes=self.track).search(MapSearch.State(self.start, 0, 0))

    def cheat_count(self, max_dist=20, min_save=100):
        count = 0
        for t1 in self.track:
            for dx in range(0, max_dist + 1):
                for dy in (
                    range(-max_dist + abs(dx), max_dist + 1 - abs(dx))
                    if dx
                    else range(1, max_dist + 1)
                ):
                    if (t2 := Point(t1.x + dx, t1.y + dy)) not in self.track:
                        continue
                    if abs(self.dist[t2] - self.dist[t1]) - abs(dx) - abs(dy) >= min_save:
                        count += 1
        return count


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RaceCondition("sample1.txt").cheat_count(2, 1) == 44
    assert RaceCondition("sample1.txt").cheat_count(20, 50) == 285

    print("Tests passed, starting with the puzzle")

    puzzle = RaceCondition(data.input_file)

    print(puzzle.cheat_count(2, 100))
    from time import time

    t = time()
    print(puzzle.cheat_count(20, 100))
    print(time() - t)

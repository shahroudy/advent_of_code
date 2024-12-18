import re
from collections import namedtuple
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.search import Search_Dijkstra


class MinDistSearch(Search_Dijkstra):
    State = namedtuple("state", ["location", "steps"])

    def get_next_states(self, state):
        location, steps = state
        for n in location.n4():
            if (n not in self.fallen) and (n.is_inside(self)):
                yield self.State(n, steps + 1)

    def cost(self, state):
        return state.steps

    def state_core(self, state):
        return state.location


class RAMRun:
    def __init__(self, filename, max_size=70):
        lines = Path(filename).read_text().splitlines()
        self.bytes = [Point(*map(int, re.findall(r"\d+", line))) for line in lines]
        self.start = Point(0, 0)
        self.goal = Point(max_size, max_size)
        self.cols = self.rows = max_size + 1

    def min_steps_to_reach_goal(self, fallen_bytes=1024):
        search = MinDistSearch(
            goal=self.goal,
            fallen=set(self.bytes[:fallen_bytes]),
            rows=self.rows,
            cols=self.cols,
        )
        min_dist, _ = search.search(initial_state=MinDistSearch.State(self.start, 0))
        return min_dist.get(self.goal, None)

    def first_blocking_byte(self, init_fallen_bytes=1024):
        min_bound, max_bound = init_fallen_bytes, len(self.bytes)
        while min_bound < max_bound - 1:
            mid = (min_bound + max_bound) // 2
            if self.min_steps_to_reach_goal(mid):
                min_bound = mid
            else:
                max_bound = mid
        last_byte = self.bytes[min_bound]
        return f"{last_byte.x},{last_byte.y}"


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert RAMRun("sample1.txt", 6).min_steps_to_reach_goal(fallen_bytes=12) == 22
    assert RAMRun("sample1.txt", 6).first_blocking_byte(init_fallen_bytes=12) == "6,1"

    print("Tests passed, starting with the puzzle")

    puzzle = RAMRun(data.input_file)

    print(puzzle.min_steps_to_reach_goal(1024))
    print(puzzle.first_blocking_byte())

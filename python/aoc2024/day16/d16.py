from collections import deque, namedtuple
from pathlib import Path

from myutils.geometry import DIRECTIONS, TURN_LEFT, TURN_RIGHT, Point
from myutils.io_handler import get_input_data
from myutils.search import Search_Dijkstra

State = namedtuple("state", ["point", "dir", "cost"])


class MyDijkstraSearch(Search_Dijkstra):
    def get_next_states(self, state):
        next_states = []
        point, dir, cost = state
        new_point = point + DIRECTIONS[dir]
        if new_point in self.map:
            next_states.append(State(new_point, dir, cost + 1))
        next_states.append(State(point, TURN_LEFT[dir], cost + 1000))
        next_states.append(State(point, TURN_RIGHT[dir], cost + 1000))
        return next_states

    def is_goal(self, state):
        return state.point == self.goal

    def cost(self, state):
        return state.cost

    def state_core(self, state):
        return (state.point, state.dir)


class ReindeerMaze:
    def __init__(self, filename):
        self.cells = set()
        for row, line in enumerate(Path(filename).read_text().splitlines()):
            for col, ch in enumerate(line):
                p = Point(col, row)
                if ch != "#":
                    self.cells.add(p)
                if ch == "S":
                    self.start = p
                if ch == "E":
                    self.goal = p
        s = MyDijkstraSearch(start=self.start, goal=self.goal, map=self.cells)
        shortest_dist, backtrace = s.search(initial_state=State(self.start, "e", 0))

        final_states = [(self.goal, d) for d in DIRECTIONS.keys()]
        self.lowest_score = min(shortest_dist[f] for f in final_states)

        to_backtrace = deque()
        for f in final_states:
            if shortest_dist[f] == self.lowest_score:
                to_backtrace.append(f)
        best_paths_tiles = set()
        while to_backtrace:
            f = to_backtrace.popleft()
            best_paths_tiles.add(f)
            for p in backtrace[f]:
                to_backtrace.append(p)
        self.best_paths_tile_count = len({point for point, dir in best_paths_tiles})


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ReindeerMaze("sample1.txt").lowest_score == 7036
    assert ReindeerMaze("sample2.txt").lowest_score == 11048
    assert ReindeerMaze("sample1.txt").best_paths_tile_count == 45
    assert ReindeerMaze("sample2.txt").best_paths_tile_count == 64

    print("Tests passed, starting with the puzzle")

    puzzle = ReindeerMaze(data.input_file)

    print(puzzle.lowest_score)
    print(puzzle.best_paths_tile_count)

    assert puzzle.lowest_score == 89460
    assert puzzle.best_paths_tile_count == 504

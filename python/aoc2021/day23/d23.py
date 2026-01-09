from collections import namedtuple
from pathlib import Path

from myutils.geometry import Point
from myutils.io_handler import get_input_data
from myutils.search import Search_AStar
from myutils.utils import read_map_dict_of_sets_of_points


class AmphipodSearch(Search_AStar):
    State = namedtuple("state", ["board", "cost"])

    def __init__(self, initial_state):
        self.initial_state = self.State(initial_state, 0)
        self.rooms = sorted(initial_state.keys(), key=lambda p: (p.y, p.x))
        self.goal_positions = {
            "A": {p for p in self.rooms if p.x == 3 and p.y > 1},
            "B": {p for p in self.rooms if p.x == 5 and p.y > 1},
            "C": {p for p in self.rooms if p.x == 7 and p.y > 1},
            "D": {p for p in self.rooms if p.x == 9 and p.y > 1},
            ".": {p for p in self.rooms if p.y == 1},
        }
        self.move_cost = {"A": 1, "B": 10, "C": 100, "D": 1000}

    def can_move_in(self, board, amphipod):
        return all(board[p] in {amphipod, "."} for p in self.goal_positions[amphipod])

    def destination_position(self, board, amphipod):
        goals = self.goal_positions[amphipod]
        return max([p for p in goals if board[p] == "."], default=None, key=lambda p: p.y)

    def move_out_candidates(self, board):
        for amphipod in "ABCD":
            goals = self.goal_positions[amphipod]
            if any(board[g] not in {amphipod, "."} for g in goals):
                yield min([p for p in goals if board[p] != "."], key=lambda p: p.y)

    def available_hallway_positions(self, board, start_pos):
        for direction in [(-1, 0), (1, 0)]:
            p = Point(start_pos.x, 1) + direction
            while board.get(p, "#") == ".":
                if p.x not in {3, 5, 7, 9}:
                    yield p
                p += direction

    def move_in_candidates(self, board):
        for amphipod in "ABCD":
            x0 = {"A": 3, "B": 5, "C": 7, "D": 9}[amphipod]
            x = x0 - 1
            while board.get(Point(x, 1), "#") == ".":
                x -= 1
            if board.get(Point(x, 1), "#") == amphipod:
                yield Point(x, 1)
            x = x0 + 1
            while board.get(Point(x, 1), "#") == ".":
                x += 1
            if board.get(Point(x, 1), "#") == amphipod:
                yield Point(x, 1)

    def get_next_states(self, state):
        board = state.board
        for src in self.move_out_candidates(board):
            ch = board[src]
            for dest in self.available_hallway_positions(board, src):
                new_board = board.copy()
                new_board[src], new_board[dest] = ".", new_board[src]
                new_cost = state.cost + self.move_cost[ch] * src.manhattan_dist(dest)
                yield self.State(new_board, new_cost)
        for src in self.move_in_candidates(board):
            ch = board[src]
            if not self.can_move_in(board, ch):
                continue
            dest = self.destination_position(board, ch)
            new_board = board.copy()
            new_board[src], new_board[dest] = ".", new_board[src]
            new_cost = state.cost + self.move_cost[ch] * src.manhattan_dist(dest)
            yield self.State(new_board, new_cost)

    def is_goal(self, state):
        return all(p in self.goal_positions[ch] for p, ch in state.board.items())

    def heuristic(self, state):
        return sum(
            self.move_cost[a] * min(p.manhattan_dist(gp) for gp in self.goal_positions[a])
            for p, a in state.board.items()
            if a != "."
        )

    def state_core(self, state):
        return tuple(state.board[r] for r in self.rooms)


class Amphipod:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()

    def load_inputs(self, insert_extra=False):
        lines = self.input_text.splitlines()
        if insert_extra:
            lines.insert(3, "  #D#C#B#A#")
            lines.insert(4, "  #D#B#A#C#")
        text = "\n".join(lines)
        char_points, _, _ = read_map_dict_of_sets_of_points(text)
        self.init_state = {point: char for char in ".ABCD" for point in char_points[char]}

    def search_minimum_energy(self, insert_extra: bool):
        self.load_inputs(insert_extra)
        return AmphipodSearch(self.init_state).search()


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Amphipod("sample1.txt").search_minimum_energy(insert_extra=False) == 12521
    assert Amphipod("sample1.txt").search_minimum_energy(insert_extra=True) == 44169

    print("Tests passed, starting with the puzzle")

    puzzle = Amphipod(data.input_file)

    print(puzzle.search_minimum_energy(insert_extra=False))
    print(puzzle.search_minimum_energy(insert_extra=True))

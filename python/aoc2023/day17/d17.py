import heapq as hq
import os
from collections import defaultdict
from pathlib import Path
from myutils.io_handler import get_input_data


class ClumsyCrucible:
    def __init__(self, filename):
        self.map = dict()
        for row, line in enumerate(Path(filename).read_text().strip().splitlines()):
            for col, ch in enumerate(line):
                self.map[(col, row)] = int(ch)
        self.destination = (col, row)
        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}

    def reset_heap(self, init_state, init_cost):
        self.state_memory = defaultdict(list)
        self.values = [init_cost]
        self.state_memory[0].append(init_state)
        self.state_history = set()
        hq.heapify(self.values)

    def push_state(self, state):
        state, cost = state[:-1], state[-1]
        if state not in self.state_history:
            hq.heappush(self.values, cost)
            self.state_memory[cost].append(state)
            self.state_history.add(state)

    def pop_state(self):
        cost = hq.heappop(self.values)
        state = self.state_memory[cost].pop()
        return (*state, cost)

    def next_states(self, state, min_str_steps=1, max_str_steps=3):
        x, y, steps, last_move, cost = state
        for move, dir in self.directions.items():
            if last_move + move in ["ns", "sn", "we", "ew"]:  # we can't reverse
                continue
            step_size = 1 if move == last_move else min_str_steps
            next_steps = steps + 1 if move == last_move else step_size
            if next_steps > max_str_steps:
                continue
            next = (x + dir[0] * step_size, y + dir[1] * step_size)
            if next not in self.map:
                continue
            next_cost = cost + sum(
                self.map[x + dir[0] * s, y + dir[1] * s] for s in range(1, step_size + 1)
            )
            yield ((*next, next_steps, move, next_cost))

    def minimum_heat_loss(self, min_str_steps=1, max_str_steps=3):
        self.reset_heap(init_state=(0, 0, 0, "0"), init_cost=0)
        while True:
            for next in self.next_states(self.pop_state(), min_str_steps, max_str_steps):
                if next[:2] == self.destination:
                    return next[-1]
                self.push_state(next)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = ClumsyCrucible(filename)
    assert answer1 is None or test.minimum_heat_loss() == answer1
    assert answer2 is None or test.minimum_heat_loss(4, 10) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 102, 94)
    test_samples("sample2.txt", None, 71)

    print("Tests passed, starting with the puzzle")

    puzzle = ClumsyCrucible(data.input_file)
    print(puzzle.minimum_heat_loss())
    print(puzzle.minimum_heat_loss(4, 10))

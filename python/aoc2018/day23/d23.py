import re
from collections import namedtuple
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data

State = namedtuple("state", ["nanobots", "nanobot_count", "lower", "higher"])


class ExperimentalEmergencyTeleportation:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        self.nanobots = [list(map(int, re.findall(r"-?\d+", line))) for line in lines]

    def nanobots_in_range_of_strongest(self):
        strongest = max(self.nanobots, key=lambda x: x[3])
        return sum(
            [
                sum(abs(i - j) for i, j in zip(strongest[:3], nanobot[:3])) <= strongest[3]
                for nanobot in self.nanobots
            ]
        )

    def get_next_states(self, state):
        for nanobot_number, (lower, higher) in enumerate(self.nanobot_bounds):
            binary_mask = 1 << nanobot_number
            if nanobot_number & state.nanobots:
                continue  # this nanobot is already in the state
            next_nanobots = state.nanobots | binary_mask
            next_lower = [max(state.lower[j], lower[j]) for j in range(4)]
            next_higher = [min(state.higher[j], higher[j]) for j in range(4)]
            if any(next_lower[j] > next_higher[j] for j in range(4)):
                continue  # no more intersection in the 3D space, this state is invalid
            yield State(next_nanobots, state.nanobot_count + 1, next_lower, next_higher)

    def search(self, initial_state):
        stack = [initial_state]
        history = set()
        max_nanobots = 0
        best = None
        while stack:
            state = stack.pop()
            stack = [s for s in stack if s.nanobots | state.nanobots != state.nanobots]
            if best is not None and (state.nanobots | best.nanobots == best.nanobots):
                continue
            for next_state in self.get_next_states(state):
                if next_state.nanobots in history:
                    continue
                stack.append(next_state)
                history.add(next_state.nanobots)
                if next_state.nanobot_count > max_nanobots:
                    max_nanobots = next_state.nanobot_count
                    best = next_state
        return best

    def in_range_of_max_nanobots(self):
        self.nanobot_bounds = []
        for x, y, z, r in self.nanobots:
            new_dims = [x + y - z, x - y + z, -x + y + z, x + y + z]
            lower, higher = [d - r for d in new_dims], [d + r for d in new_dims]
            self.nanobot_bounds.append([lower, higher])

        best = self.search(State(0, 0, [float("-inf")] * 4, [float("inf")] * 4))

        min_distance = float("inf")
        for a, b, c, d in product(*(range(best.lower[i], best.higher[i] + 1) for i in range(4))):
            if (d - a) % 2 == 0 and (d - c) % 2 == 0 and (d - b) % 2 == 0:
                x, y, z = (d - c) // 2, (d - b) // 2, (d - a) // 2
                min_distance = min(min_distance, (abs(x) + abs(y) + abs(z)))
        return min_distance

    def in_range_of_max_nanobots_hack(self):
        ranges = []
        bounds = set()
        for x, y, z, r in self.nanobots:
            d = abs(x) + abs(y) + abs(z)
            min_max = (max(0, d - r), d + r)
            ranges.append(min_max)
            bounds |= set(min_max)
        result = 0
        max_count = 0
        for b in sorted(bounds):
            count = sum(l <= b <= r for l, r in ranges)
            if count > max_count:
                result = b
                max_count = count
        return result


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ExperimentalEmergencyTeleportation("sample1.txt").nanobots_in_range_of_strongest() == 7
    assert ExperimentalEmergencyTeleportation("sample2.txt").in_range_of_max_nanobots() == 36

    print("Tests passed, starting with the puzzle")

    puzzle = ExperimentalEmergencyTeleportation(data.input_file)

    print(puzzle.nanobots_in_range_of_strongest())
    print(puzzle.in_range_of_max_nanobots())
    print(puzzle.in_range_of_max_nanobots_hack())

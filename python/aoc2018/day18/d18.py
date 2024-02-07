from collections import Counter
from itertools import product
from pathlib import Path

from myutils.io_handler import get_input_data


class SettlersOfTheNorthPole:
    def __init__(self, filename):
        lines = Path(filename).read_text().splitlines()
        rows, cols = len(lines), len(lines[0])
        self.state = "".join(lines)
        self.adj = dict()
        mask8 = [c for c in product(range(-1, 2), range(-1, 2)) if any(c)]
        idx = lambda x, y: x + y * cols
        for x, y in product(range(cols), range(rows)):
            adj = [(x + dx, y + dy) for dx, dy in mask8]
            self.adj[idx(x, y)] = [idx(a, b) for a, b in adj if 0 <= a < cols and 0 <= b < rows]

    def simulate(self, minutes=10):
        state = self.state
        history = {}
        fast_forwarded = False
        minute = 0
        while minute < minutes:
            next_state = ""
            for i in range(len(state)):
                counts = Counter(state[j] for j in self.adj[i])
                if state[i] == ".":
                    next_state += "|" if counts["|"] >= 3 else "."
                elif state[i] == "|":
                    next_state += "#" if counts["#"] >= 3 else "|"
                else:
                    next_state += "#" if counts["#"] >= 1 and counts["|"] >= 1 else "."
            state = next_state
            minute += 1
            if not fast_forwarded:
                if state in history:
                    cycle = minute - history[state]
                    minute += ((minutes - minute) // cycle) * cycle
                    fast_forwarded = True
                else:
                    history[state] = minute
        return state.count("|") * state.count("#")


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SettlersOfTheNorthPole("sample1.txt").simulate() == 1147

    print("Tests passed, starting with the puzzle")

    puzzle = SettlersOfTheNorthPole(data.input_file)
    print(puzzle.simulate())
    print(puzzle.simulate(minutes=1000000000))

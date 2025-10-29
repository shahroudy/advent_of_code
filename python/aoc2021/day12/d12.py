from collections import defaultdict, namedtuple
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.search import Search_All_Goals
from myutils.utils import find_all_re


class PathSearch(Search_All_Goals):
    State = namedtuple("state", ["repeated_count", "path"])

    def get_next_states(self, state):
        current = state.path[-1]
        for next in self.connections[current] - {"start"}:
            if next.islower() and next in state.path:
                if state.repeated_count < self.allowed_repeats:
                    yield PathSearch.State(state.repeated_count + 1, state.path + (next,))
            else:
                yield PathSearch.State(state.repeated_count, state.path + (next,))

    def get_result(self, state):
        return "-".join(state.path)

    def is_goal(self, state):
        return state.path[-1] == "end"


class PassagePathing:
    def __init__(self, filename):
        self.connections = defaultdict(set)
        for a, b in find_all_re(r"(\w+)-(\w+)", text=Path(filename).read_text()):
            self.connections[a].add(b)
            self.connections[b].add(a)

    def path_count(self, allowed_repeats=0):
        search = PathSearch(connections=self.connections, allowed_repeats=allowed_repeats)
        return len(search.search(initial_state=PathSearch.State(0, ("start",))))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PassagePathing("sample1.txt").path_count(allowed_repeats=0) == 10
    assert PassagePathing("sample2.txt").path_count(allowed_repeats=0) == 19
    assert PassagePathing("sample3.txt").path_count(allowed_repeats=0) == 226

    assert PassagePathing("sample1.txt").path_count(allowed_repeats=1) == 36
    assert PassagePathing("sample2.txt").path_count(allowed_repeats=1) == 103
    assert PassagePathing("sample3.txt").path_count(allowed_repeats=1) == 3509

    print("Tests passed, starting with the puzzle")

    puzzle = PassagePathing(data.input_file)

    print(puzzle.path_count(allowed_repeats=0))
    print(puzzle.path_count(allowed_repeats=1))

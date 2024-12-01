import os
from collections import deque
from pathlib import Path
from myutils.io_handler import get_input_data


class MemoryManeuver:
    def __init__(self, filename):
        self.nums = list(map(int, Path(filename).read_text().strip().split()))
        self.process()

    def read_node_from_tape(self):
        self.node_counter += 1
        id = self.node_counter
        nc = self.tape.popleft()
        nm = self.tape.popleft()
        children = [self.read_node_from_tape() for _ in range(nc)]
        meta = [self.tape.popleft() for _ in range(nm)]
        self.tree[id] = [children, meta]
        return id

    def process(self):
        self.tape = deque(self.nums)
        self.node_counter = 0
        self.tree = {}
        self.read_node_from_tape()

    def sum_metadata(self):
        return sum([sum(v[1]) for v in self.tree.values()])

    def evaluate(self, index):
        children, metadata = self.tree[index]
        if children:
            return sum(
                [self.evaluate(children[c - 1]) for c in metadata if c > 0 and c <= len(children)]
            )
        else:
            return sum(metadata)

    def root_value(self):
        return self.evaluate(1)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = MemoryManeuver("test1.txt")
    assert test1.sum_metadata() == 138
    assert test1.root_value() == 66

    memory_maneuver = MemoryManeuver(data.input_file)
    print(memory_maneuver.sum_metadata())
    print(memory_maneuver.root_value())

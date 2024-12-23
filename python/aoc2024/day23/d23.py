import re
from collections import defaultdict
from functools import reduce
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class LANParty:
    def __init__(self, filename):
        pairs = {tuple(re.findall(r"(\w+)", ln)) for ln in Path(filename).read_text().splitlines()}
        connected = defaultdict(set)
        for n, m in pairs:
            connected[n].add(m)
            connected[m].add(n)

        self.interconnected = {2: pairs}
        for level in count(3):
            self.interconnected[level] = set()
            for group in self.interconnected[level - 1]:
                for to_add in reduce(set.intersection, (connected[node] for node in group)):
                    self.interconnected[level].add(tuple(sorted(set(group) | {to_add})))
            if len(self.interconnected[level]) == 0:
                self.max_level = level - 1
                break

    def triple_count_with_t(self):
        return sum(any(node.startswith("t") for node in group) for group in self.interconnected[3])

    def password(self):
        return ",".join(self.interconnected[self.max_level].copy().pop())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert LANParty("sample1.txt").triple_count_with_t() == 7
    assert LANParty("sample1.txt").password() == "co,de,ka,ta"

    print("Tests passed, starting with the puzzle")

    puzzle = LANParty(data.input_file)

    print(puzzle.triple_count_with_t())
    print(puzzle.password())

import os
from collections import defaultdict, deque, Counter
from myutils.file_reader import read_lines


class PassagePathing:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.process()

    def process(self):
        self.dest = defaultdict(list)
        for line in self.lines:
            left, right = line.split("-")
            for source, dest in [[left, right], [right, left]]:
                if dest != "start" and source != "end":
                    self.dest[source].append(dest)

    def count_paths(self, single_small_twice=False):
        queue = deque()
        queue.append(["start"])
        paths = 0
        while queue:
            current_path = queue.popleft()
            for cave in self.dest[current_path[-1]]:
                if cave == "end":
                    paths += 1
                    continue
                if cave.islower() and cave in current_path:
                    if single_small_twice:
                        lower_counts = Counter(
                            [c for c in current_path if c.islower()]
                        )
                        if max(lower_counts.values()) > 1:
                            continue
                    else:
                        continue
                queue.append(current_path + [cave])
        return paths


if __name__ == "__main__":
    test1 = PassagePathing("test1.txt")
    assert test1.count_paths() == 10
    assert test1.count_paths(single_small_twice=True) == 36
    test2 = PassagePathing("test2.txt")
    assert test2.count_paths() == 19
    assert test2.count_paths(single_small_twice=True) == 103
    test3 = PassagePathing("test3.txt")
    assert test3.count_paths() == 226
    assert test3.count_paths(single_small_twice=True) == 3509

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day12.txt'
    passage_pathing = PassagePathing(input_file)
    print(passage_pathing.count_paths())
    print(passage_pathing.count_paths(True))

import os
import re
from pathlib import Path
from collections import defaultdict
from myutils.io_handler import get_input_data


class TheSumOfItsParts:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        dependency = defaultdict(list)
        input_regex = re.compile(r"Step (\w) must be finished before step (\w) can begin.")
        self.signs = set()
        for line in self.lines:
            req, depenent = input_regex.match(line).groups()
            dependency[depenent].append(req)
            self.signs.update({req, depenent})
        self.dependency = dict(dependency)

    def order_of_single_steps(self):
        result = []
        signs = self.signs.copy()
        dependency = self.dependency.copy()
        while signs:
            possible = list(signs - set(dependency.keys()))
            s = min(possible)
            signs.remove(s)
            result.append(s)
            # remove dependencies to s
            dependency = {k: [i for i in v if i != s] for k, v in dependency.items()}
            # remove available sings
            dependency = {k: v for k, v in dependency.items() if v}
        return "".join(result)

    def time_needed(self, sign, bias):
        return bias + 1 + ord(sign) - ord("A")

    def time_to_complete_with_workers(self, workers_count=2, bias=0):
        signs = self.signs.copy()
        dependencies = self.dependency.copy()
        time = 0
        workers = {}
        while signs or workers:
            possible = list(signs - set(dependencies.keys()))
            possible.sort(reverse=True)

            while len(workers) < workers_count and possible:
                s = possible.pop()
                workers[s] = self.time_needed(s, bias)
                signs.remove(s)

            step = min(workers.values())
            time += step
            for w in list(workers.keys()):
                workers[w] -= step
                if workers[w] == 0:
                    del workers[w]
                    # remove dependencies to s
                    dependencies = {k: [i for i in v if i != w] for k, v in dependencies.items()}
                    # remove available sings
                    dependencies = {k: v for k, v in dependencies.items() if v}
        return time


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = TheSumOfItsParts("test1.txt")
    assert test1.order_of_single_steps() == "CABDFE"
    assert test1.time_to_complete_with_workers() == 15

    the_sum_of_its_parts = TheSumOfItsParts(data.input_file)
    print(the_sum_of_its_parts.order_of_single_steps())
    print(the_sum_of_its_parts.time_to_complete_with_workers(5, 60))

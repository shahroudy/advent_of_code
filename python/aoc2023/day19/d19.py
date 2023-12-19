import os
import re
from functools import reduce
from pathlib import Path


class Aplenty:
    def __init__(self, filename):
        wf_lines, p_lines = [g.splitlines() for g in Path(filename).read_text().split("\n\n")]

        self.workflows = {}
        workflow_re = re.compile(r"(\w+)\{(.+)\}")
        for workflow in wf_lines:
            name, rules = re.match(workflow_re, workflow).groups()
            rules = re.split(",", rules)
            self.workflows[name] = [tuple(r.split(":")) for r in rules[:-1]] + [("True", rules[-1])]

        parts_re = re.compile(r"(\w+)=(-?\d+)")
        self.parts = [{cat: int(rate) for cat, rate in re.findall(parts_re, i)} for i in p_lines]

    def sum_rating_accepted_parts(self):
        rating_sum = 0
        for part in self.parts:
            state = "in"
            while state not in "AR":
                for condition, new_state in self.workflows[state]:
                    if eval(condition, None, part):
                        state = new_state
                        break
            if state == "A":
                rating_sum += sum(part.values())
        return rating_sum

    def apply_workflow(self, part_range, name):
        new_part_ranges = []
        for condition, new_state in self.workflows[name]:
            if condition == "True":
                new_part_ranges.append((part_range, new_state))
                return new_part_ranges
            cat, operator, value = condition[0], condition[1], int(condition[2:])
            start, end = part_range[cat]
            if start <= value <= end:
                new_range = part_range.copy()
                part_range[cat] = (value, end) if operator == "<" else (start, value)
                new_range[cat] = (start, value - 1) if operator == "<" else (value + 1, end)
                new_part_ranges.append((new_range, new_state))

    def count_accepted_distinct_combinations(self):
        cnt = 0
        full_range = (1, 4000)
        part_ranges = [({cat: full_range for cat in "xmas"}, "in")]
        while part_ranges:
            for p_rng, name in self.apply_workflow(*part_ranges.pop()):
                if name == "A":
                    cnt += reduce(lambda x, y: x * y, [e - b + 1 for b, e in p_rng.values()])
                elif name != "R":
                    part_ranges.append((p_rng, name))
        return cnt


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Aplenty(filename)
    assert answer1 is None or test.sum_rating_accepted_parts() == answer1
    assert answer2 is None or test.count_accepted_distinct_combinations() == answer2


if __name__ == "__main__":
    test_samples("sample1.txt", 19114, 167409079868000)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2023_day19.txt'
    puzzle = Aplenty(input_file)
    print(puzzle.sum_rating_accepted_parts())
    print(puzzle.count_accepted_distinct_combinations())

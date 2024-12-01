import os
from pathlib import Path
from myutils.io_handler import get_input_data


class HexEd:
    def __init__(self, filename):
        directions = ["n", "nw", "sw", "s", "se", "ne"]
        dir_index = {directions[i]: i for i in range(6)}
        step_counts = [0] * 6
        self.farthest_dist = 0
        for step in Path(filename).read_text().strip().split(","):
            d = dir_index[step]
            if step_counts[(d + 3) % 6] > 0:  # cancel an opposite step
                step_counts[(d + 3) % 6] -= 1
            elif step_counts[(d - 2) % 6] > 0:  # move a -2 step to a -1 step
                step_counts[(d - 2) % 6] -= 1
                step_counts[(d - 1) % 6] += 1
            elif step_counts[(d + 2) % 6] > 0:  # move a +2 step to a +1 step
                step_counts[(d + 2) % 6] -= 1
                step_counts[(d + 1) % 6] += 1
            else:  # otherwise, move one step towards this direction
                step_counts[d] += 1
            self.farthest_dist = max(self.farthest_dist, sum(step_counts))
        self.final_dist = sum(step_counts)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = HexEd(filename)
    assert answer1 is None or test.final_dist == answer1
    assert answer2 is None or test.farthest_dist == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 3, None)
    test_samples("sample2.txt", 0, None)
    test_samples("sample3.txt", 2, None)
    test_samples("sample4.txt", 3, None)

    print("Tests passed, starting with the puzzle")

    puzzle = HexEd(data.input_file)
    print(puzzle.final_dist)
    print(puzzle.farthest_dist)

import os
from pathlib import Path
from numpy import sign
from myutils.io_handler import get_input_data


class RopeBridge:
    def __init__(self, filename):
        self.moves = []
        for line in Path(filename).read_text().strip().split("\n"):
            direction, length = line.split()
            self.moves.append([direction, int(length)])

    def pull_the_damn_rope(self, num_knots=2):
        knots = [[0, 0] for _ in range(num_knots)]
        tail_positions = set()
        delta = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
        for direction, length in self.moves:
            for _ in range(length):
                knots[0] = [knots[0][j] + delta[direction][j] for j in range(2)]
                for k in range(1, num_knots):
                    if any([abs(knots[k - 1][j] - knots[k][j]) > 1 for j in range(2)]):
                        for dim in range(2):
                            knots[k][dim] += sign(knots[k - 1][dim] - knots[k][dim])
                tail_positions.add(tuple(knots[-1]))
        return len(tail_positions)


def test_samples(filename, parameter, answer):
    test = RopeBridge(filename)
    assert test.pull_the_damn_rope(parameter) == answer


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 2, 13)
    test_samples("sample2.txt", 10, 36)

    rope_bridge = RopeBridge(data.input_file)
    print(rope_bridge.pull_the_damn_rope())
    print(rope_bridge.pull_the_damn_rope(10))

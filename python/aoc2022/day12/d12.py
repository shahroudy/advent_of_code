import os
from collections import deque
from pathlib import Path


class HillClimbingAlgorithm:
    def __init__(self, filename):
        lines = Path(filename).read_text().strip().split("\n")
        char_map = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
        self.map = dict()
        for p, c in char_map.items():
            if c == "S":
                self.start = p
                c = "a"
            elif c == "E":
                self.end = p
                c = "z"
            self.map[p] = ord(c) - ord("a")

    def dist_to_E(self, start):
        queue = deque()
        distance = {start: 0}
        queue.append(start)
        while queue:
            current_point = queue.popleft()
            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = tuple([current_point[i] + direction[i] for i in range(2)])
                if neighbor not in self.map:
                    continue
                if self.map[neighbor] - self.map[current_point] <= 1 and neighbor not in distance:
                    distance[neighbor] = distance[current_point] + 1
                    if neighbor == self.end:
                        return distance[neighbor]
                    queue.append(neighbor)
        return float("inf")

    def start_to_E_dist(self):
        return self.dist_to_E(self.start)

    def min_a_to_E_dist(self):
        return min([self.dist_to_E(start) for start, height in self.map.items() if height == 0])


def test_samples(filename, answer1, answer2):
    test = HillClimbingAlgorithm(filename)
    assert test.start_to_E_dist() == answer1
    assert test.min_a_to_E_dist() == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", 31, 29)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day12.txt'
    puzzle = HillClimbingAlgorithm(input_file)
    print(puzzle.start_to_E_dist())
    print(puzzle.min_a_to_E_dist())

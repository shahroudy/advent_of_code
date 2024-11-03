from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class SporificaVirus:
    def __init__(self, filename):
        self.directions = {"e": (1, 0), "w": (-1, 0), "n": (0, -1), "s": (0, 1)}
        self.turn_left = {"e": "n", "n": "w", "w": "s", "s": "e"}
        self.turn_right = {"e": "s", "s": "w", "w": "n", "n": "e"}
        self.turn_reverse = {"e": "w", "w": "e", "n": "s", "s": "n"}
        lines = Path(filename).read_text().splitlines()
        self.map = dict()
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                self.map[(col, row)] = ch == "#"
        self.rows, self.cols = row + 1, col + 1

    def count_infection_bursts(self, bursts=10000):
        cur, d, infections_count = (self.cols // 2, self.rows // 2), "n", 0
        map = defaultdict(bool, self.map)
        for _ in range(bursts):
            d = self.turn_right[d] if map[cur] else self.turn_left[d]
            map[cur] = not map[cur]
            if map[cur]:
                infections_count += 1
            cur = tuple(cur[i] + self.directions[d][i] for i in range(2))
        return infections_count

    def count_infection_bursts_evolved(self, bursts=10000000):
        cur, d, infections_count = (self.cols // 2, self.rows // 2), "n", 0
        map = defaultdict(int, {p: 2 if v else 0 for p, v in self.map.items()})
        for _ in range(bursts):
            state = map[cur]
            if state == 0:
                d = self.turn_left[d]
            elif state == 2:
                d = self.turn_right[d]
            elif state == 3:
                d = self.turn_reverse[d]
            if state == 1:
                infections_count += 1
            map[cur] = (state + 1) % 4
            cur = tuple(cur[i] + self.directions[d][i] for i in range(2))
        return infections_count


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SporificaVirus("sample1.txt").count_infection_bursts(7) == 5
    assert SporificaVirus("sample1.txt").count_infection_bursts(70) == 41
    assert SporificaVirus("sample1.txt").count_infection_bursts(10000) == 5587
    assert SporificaVirus("sample1.txt").count_infection_bursts_evolved(100) == 26
    assert SporificaVirus("sample1.txt").count_infection_bursts_evolved(10000000) == 2511944

    print("Tests passed, starting with the puzzle")

    puzzle = SporificaVirus(data.input_file)

    print(puzzle.count_infection_bursts())
    print(puzzle.count_infection_bursts_evolved())

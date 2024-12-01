import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class PacketScanners:
    def __init__(self, filename):
        self.depth = {}
        for line in Path(filename).read_text().strip().split("\n"):
            layer_no, depth = map(int, re.findall(r"\d+", line))
            self.depth[layer_no] = depth
        self.loop_time = {k: 2 * (v - 1) for k, v in self.depth.items()}
        self.layer_count = 1 + max(self.loop_time.keys())

    def trip_severity(self):
        res = 0
        for p in range(self.layer_count):
            if p in self.loop_time and p % self.loop_time[p] == 0:
                res += p * self.depth[p]
        return res

    def delay_not_to_get_caught(self):
        delay = 0
        while True:
            for p in range(self.layer_count):
                if p in self.loop_time and (p + delay) % self.loop_time[p] == 0:
                    delay += 1
                    break
            else:
                return delay


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = PacketScanners(filename)
    assert answer1 is None or test.trip_severity() == answer1
    assert answer2 is None or test.delay_not_to_get_caught() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)
    test_samples("sample1.txt", 24, 10)

    print("Tests passed, starting with the puzzle")

    puzzle = PacketScanners(data.input_file)
    print(puzzle.trip_severity())
    print(puzzle.delay_not_to_get_caught())

import os
import re
from pathlib import Path
from myutils.io_handler import get_input_data


class BeaconExclusionZone:
    def __init__(self, filename):
        self.close = dict()

        line_re = re.compile(r"Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+).*")
        for line in Path(filename).read_text().strip().split("\n"):
            nums = list(map(int, line_re.match(line).groups()))
            self.close[tuple(nums[:2])] = tuple(nums[2:])

    def no_beacon_count_in_row(self, row=10):
        res = set()
        for s, b in self.close.items():
            d = abs(s[0] - b[0]) + abs(s[1] - b[1])
            for x in range(d + 1):
                if abs(row - s[1]) <= d - x:
                    res.add(s[0] + x)
                    res.add(s[0] - x)
        return len([r for r in res if (r, row) not in self.close.values()])

    def tuning_freq_of_hidden_beacon(self, max_range=20):
        for s, b in self.close.items():
            cd = abs(b[0] - s[0]) + abs(b[1] - s[1]) + 1
            for x in range(cd + 1):
                y = cd - x
                for xx in (s[0] + x, s[0] - x):
                    for yy in (s[1] + y, s[1] - y):
                        if xx >= 0 and xx <= max_range and yy >= 0 and yy <= max_range:
                            for ss, bb in self.close.items():
                                db = abs(ss[0] - bb[0]) + abs(ss[1] - bb[1])
                                d = abs(xx - ss[0]) + abs(yy - ss[1])
                                if d <= db:
                                    break
                            else:
                                return xx * 4000000 + yy


def test_samples(filename, answer1, answer2):
    test = BeaconExclusionZone(filename)
    assert test.no_beacon_count_in_row() == answer1
    assert test.tuning_freq_of_hidden_beacon() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 26, 56000011)

    beacon_exclusion_zone = BeaconExclusionZone(data.input_file)
    print(beacon_exclusion_zone.no_beacon_count_in_row(2000000))
    print(beacon_exclusion_zone.tuning_freq_of_hidden_beacon(4000000))

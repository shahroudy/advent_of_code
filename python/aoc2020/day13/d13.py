from itertools import count
from math import lcm
from pathlib import Path

from myutils.io_handler import get_input_data


class ShuttleSearch:
    def __init__(self, filename):
        earliest, bus_IDs = Path(filename).read_text().splitlines()
        self.earliest = int(earliest)
        self.bus_IDs = [(int(id), i) for i, id in enumerate(bus_IDs.split(",")) if id != "x"]

    def earliest_bus(self):
        for time in count():
            for bus, _ in self.bus_IDs:
                if (time + self.earliest) % bus == 0:
                    return bus * time

    def earliest_match_time(self):
        earliest, step = 0, 1
        for bus_id, time in self.bus_IDs:
            while (earliest % bus_id) != (-time % bus_id):
                earliest += step
            step = lcm(step, bus_id)
        return earliest


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert ShuttleSearch("sample1.txt").earliest_bus() == 295
    assert ShuttleSearch("sample1.txt").earliest_match_time() == 1068781
    assert ShuttleSearch("sample2.txt").earliest_match_time() == 3417
    assert ShuttleSearch("sample3.txt").earliest_match_time() == 754018
    assert ShuttleSearch("sample4.txt").earliest_match_time() == 779210
    assert ShuttleSearch("sample5.txt").earliest_match_time() == 1261476
    assert ShuttleSearch("sample6.txt").earliest_match_time() == 1202161486

    print("Tests passed, starting with the puzzle")

    puzzle = ShuttleSearch(data.input_file)

    print(puzzle.earliest_bus())
    print(puzzle.earliest_match_time())

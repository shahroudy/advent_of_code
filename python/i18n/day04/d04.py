import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


class ATripAroundTheWorld:
    def __init__(self, filename):
        self.trips = Path(filename).read_text().split("\n\n")

    def sum_of_travel_time(self):
        s = 0
        for trip in self.trips:
            dates = []
            for info in trip.splitlines():
                _, c, t = info.split(maxsplit=2)
                dates.append(datetime.strptime(t, "%b %d, %Y, %H:%M").replace(tzinfo=ZoneInfo(c)))
            s += int((dates[1] - dates[0]).total_seconds())
        return s // 60


if __name__ == "__main__":
    assert ATripAroundTheWorld("test-input.txt").sum_of_travel_time() == 3143
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(ATripAroundTheWorld(f"{input_folder}/i18n2025_day04.txt").sum_of_travel_time())

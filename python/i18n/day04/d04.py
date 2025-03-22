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
    assert ATripAroundTheWorld("test-input").sum_of_travel_time() == 3143
    print("Tests passed, starting with the puzzle")
    print(ATripAroundTheWorld("input").sum_of_travel_time())

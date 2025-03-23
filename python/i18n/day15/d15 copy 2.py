import os
import re
from datetime import UTC, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from myutils.exrange import ExRange


class Puzzle:
    def __init__(self, filename):
        services, offices = Path(filename).read_text().split("\n\n")
        regex = re.compile(r"^.+\t(.+)\t(.+)$")
        self.service = []
        for line in services.splitlines():
            parts = line.split("\t")
            tz = parts[1]
            holidays = parts[2].split(";")
            self.service.append([tz, holidays])
        self.office = []
        for line in offices.splitlines():
            parts = line.split("\t")
            tz = parts[1]
            holidays = parts[2].split(";")
            self.office.append([tz, holidays])

    def get_minutes_ranges_in_2022(self, tz, holidays, office_hours):
        origin = datetime(year=2022, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        all_minutes = ExRange()

        timezone = ZoneInfo(tz)
        h = []
        for holiday in holidays:
            date = datetime.strptime(holiday, "%d %B %Y").replace(tzinfo=timezone)
            h.append(date)

        start_hour, start_min = (8, 30) if office_hours else (0, 0)
        start = datetime(2021, 12, 1, start_hour, start_min, tzinfo=timezone)
        end = start + (timedelta(hours=8, minutes=30) if office_hours else timedelta(hours=24))

        while start < datetime(2023, 2, 1, tzinfo=timezone):
            if (start.date() not in h) and (start.weekday() < 5):
                start_utc = start.astimezone(UTC)
                end_utc = end.astimezone(UTC)
                start_minutes = int((start_utc - origin).total_seconds() // 60)
                stop_minutes = int((end_utc - origin).total_seconds() // 60)
                all_minutes.add(range(int(start_minutes), int(stop_minutes)))
            start += timedelta(days=1)
            end += timedelta(days=1)
        return all_minutes

    def calc(self):
        origin = datetime(year=2022, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        end_origin = datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        startm = int((origin - origin).total_seconds() // 60)
        endm = int((end_origin - origin).total_seconds() // 60)
        ref_minutes = range(int(startm), int(endm))

        service_minutes = ExRange()
        for tz, holidays in self.service:
            service_minutes.add(self.get_minutes_ranges_in_2022(tz, holidays, True))

        diffs = []
        for tz, holidays in self.office:
            request_minutes = self.get_minutes_ranges_in_2022(tz, holidays, False)
            request_minutes.intersect(ref_minutes)
            request_minutes -= service_minutes
            diff = request_minutes.length()
            diffs.append(diff)

        return max(diffs) - min(diffs)


if __name__ == "__main__":
    assert Puzzle("test-input.txt").calc() == 3030
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(Puzzle(f"{input_folder}/i18n2025_day15.txt").calc())

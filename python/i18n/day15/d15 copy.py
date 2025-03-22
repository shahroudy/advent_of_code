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

    def calc(self):
        origin = datetime(year=2022, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        end_origin = datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0, tzinfo=UTC)
        startm = int((origin - origin).total_seconds() // 60)
        endm = int((end_origin - origin).total_seconds() // 60)
        ref_minutes = range(int(startm), int(endm))

        service_minutes = ExRange()
        for tz, holidays in self.service:
            timezone = ZoneInfo(tz)
            h = []
            for holiday in holidays:
                date = datetime.strptime(holiday, "%d %B %Y").replace(tzinfo=timezone)
                h.append(date)
            for year in range(2021, 2024):
                for month in range(1, 13):
                    for day in range(1, 32):
                        try:
                            date = datetime(year=year, month=month, day=day, tzinfo=timezone)
                        except ValueError:
                            continue  # if the date is invalid, skip it
                        if date in h:
                            continue
                        if date.weekday() >= 5:
                            continue
                        start = datetime(
                            year=year,
                            month=month,
                            day=day,
                            hour=8,
                            minute=30,
                            second=0,
                            tzinfo=timezone,
                        ).astimezone(UTC)
                        stop = datetime(
                            year=year,
                            month=month,
                            day=day,
                            hour=17,
                            minute=00,
                            second=0,
                            tzinfo=timezone,
                        ).astimezone(UTC)
                        startm = int((start - origin).total_seconds() // 60)
                        stopm = int((stop - origin).total_seconds() // 60)
                        service_minutes.add(range(int(startm), int(stopm)))

        diffs = []
        for tz, holidays in self.office:
            timezone = ZoneInfo(tz)
            h = []
            for holiday in holidays:
                date = datetime.strptime(holiday, "%d %B %Y").replace(tzinfo=timezone)
                h.append(date)
            office_minutes = ExRange()
            for year in range(2021, 2024):
                for month in range(1, 13):
                    for day in range(1, 32):
                        try:
                            date = datetime(year=year, month=month, day=day, tzinfo=timezone)
                        except ValueError:
                            continue  # if the date is invalid, skip it
                        if date in h:
                            continue
                        if date.weekday() >= 5:
                            continue
                        start = datetime(
                            year=year,
                            month=month,
                            day=day,
                            hour=0,
                            minute=0,
                            second=0,
                            tzinfo=timezone,
                        ).astimezone(UTC)
                        stop = start + timedelta(days=1)
                        startm = int((start - origin).total_seconds() // 60)
                        stopm = int((stop - origin).total_seconds() // 60)
                        office_minutes.add(range(int(startm), int(stopm)))
            office_minutes.intersect(ref_minutes)
            office_minutes -= service_minutes
            diff = office_minutes.length()
            diffs.append(diff)

        return max(diffs) - min(diffs)


if __name__ == "__main__":
    assert Puzzle("test-input").calc() == 3030
    print("Tests passed, starting with the puzzle")
    print(Puzzle("input").calc())

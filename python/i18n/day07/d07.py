import os
from datetime import UTC, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


class TheAuditTrailFixer:
    def __init__(self, filename):
        self.inp = Path(filename).read_text().splitlines()

    def calc(self):
        line_no = 0
        hal_zone = ZoneInfo("America/Halifax")
        san_zone = ZoneInfo("America/Santiago")
        result = 0
        for line_no, line in enumerate(self.inp):
            t, a, b = line.split()
            utc = datetime.strptime(t, "%Y-%m-%dT%H:%M:%S.%f%z").astimezone(UTC)
            hal_check = utc.astimezone(hal_zone).strftime("%Y-%m-%dT%H:%M:%S.000%:z")
            san_check = utc.astimezone(san_zone).strftime("%Y-%m-%dT%H:%M:%S.000%:z")
            assert t in (hal_check, san_check)
            utc = utc + timedelta(minutes=int(a) - int(b))
            correct_time = utc.astimezone(hal_zone) if hal_check == t else utc.astimezone(san_zone)
            result += correct_time.hour * (line_no + 1)
        return result


if __name__ == "__main__":
    assert TheAuditTrailFixer("test-input.txt").calc() == 866
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(TheAuditTrailFixer(f"{input_folder}/i18n2025_day07.txt").calc())

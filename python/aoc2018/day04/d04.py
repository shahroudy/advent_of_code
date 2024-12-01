import os
import re
from collections import defaultdict, Counter
from pathlib import Path
from myutils.io_handler import get_input_data


class ReposeRecord:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        self.lines.sort()
        self.sleep = defaultdict(list)
        line_re = re.compile(r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.+)")
        shift_re = re.compile(r"Guard #(\d+) begins shift")
        for line in self.lines:
            parts = line_re.match(line).groups()
            minute, event = int(parts[-2]), parts[-1]
            shift_begin = shift_re.match(event)
            if shift_begin:
                current_guard = int(shift_begin.groups()[0])
            elif event == "falls asleep":
                sleeping_minute = minute
            else:  # it's a "wakes up" event
                self.sleep[current_guard].extend(range(sleeping_minute, minute))

    def top_guard_strategy_1(self):
        max_guard = max(self.sleep.keys(), key=lambda k: len(self.sleep[k]))
        return max_guard * Counter(self.sleep[max_guard]).most_common(1)[0][0]

    def top_guard_strategy_2(self):
        max_freq = 0
        for guard_no, sleep_mins in self.sleep.items():
            minute, frequency = Counter(sleep_mins).most_common(1)[0]
            if frequency > max_freq:
                max_freq = frequency
                result = guard_no * minute
        return result


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = ReposeRecord("test1.txt")
    assert test1.top_guard_strategy_1() == 240
    assert test1.top_guard_strategy_2() == 4455

    repose_record = ReposeRecord(data.input_file)
    print(repose_record.top_guard_strategy_1())
    print(repose_record.top_guard_strategy_2())

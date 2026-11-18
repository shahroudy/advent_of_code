from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import process_int_list


class ReposeRecord:
    def __init__(self, filename):
        records = sorted(process_int_list(Path(filename).read_text(), accepted_signs=""))
        self.sleep_records = dict()
        for record in records:
            if len(record) == 6:  # new shift with a new guard id
                minute, guard_id = record[-2:]
                if guard_id not in self.sleep_records:
                    self.sleep_records[guard_id] = defaultdict(int)
                is_up = True
            else:  # same guard's new record
                minute, pre_minute = record[-1], minute
                is_up = not is_up
                if is_up:
                    for minute in range(pre_minute, minute):
                        self.sleep_records[guard_id][minute] += 1

    def sleeping_guard_strategy1(self):
        max_guard_id = max(self.sleep_records, key=lambda x: sum(self.sleep_records[x].values()))
        his_records = self.sleep_records[max_guard_id]
        max_minute = max(his_records, key=his_records.get)
        return max_guard_id * max_minute

    def sleeping_guard_strategy2(self):
        _, minute, guard_id = max(
            (count, minute, guard_id)
            for guard_id, records in self.sleep_records.items()
            for minute, count in records.items()
        )
        return minute * guard_id


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = ReposeRecord("sample1.txt")
    assert test.sleeping_guard_strategy1() == 240
    assert test.sleeping_guard_strategy2() == 4455

    print("Tests passed, starting with the puzzle")

    puzzle = ReposeRecord(data.input_file)

    print(puzzle.sleeping_guard_strategy1())
    print(puzzle.sleeping_guard_strategy2())

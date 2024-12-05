import re
from functools import cmp_to_key
from pathlib import Path

from myutils.io_handler import get_input_data


class PrintQueue:
    def __init__(self, filename):
        rules_txt, updates_txt = Path(filename).read_text().strip().split("\n\n")
        rules = {tuple(numbers) for numbers in re.findall(r"(\d+)\|(\d+)", rules_txt)}
        updates = [re.findall(r"\d+", update) for update in updates_txt.split("\n")]
        self.not_changed_medians_sum = 0
        self.changed_medians_sum = 0
        for update in updates:
            fixed = sorted(update, key=cmp_to_key(lambda x, y: 1 if (y, x) in rules else -1))
            if fixed == update:
                self.not_changed_medians_sum += int(fixed[len(fixed) // 2])
            else:
                self.changed_medians_sum += int(fixed[len(fixed) // 2])


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PrintQueue("sample1.txt").not_changed_medians_sum == 143
    assert PrintQueue("sample1.txt").changed_medians_sum == 123

    print("Tests passed, starting with the puzzle")

    puzzle = PrintQueue(data.input_file)

    print(puzzle.not_changed_medians_sum)
    print(puzzle.changed_medians_sum)

import os
from pathlib import Path


class LengthLimitsOnMessagingPlatforms:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text().splitlines()

    def total_cost(self):
        cost = 0
        for line in self.input_text:
            chars, bytes = len(line), len(line.encode("utf-8"))
            cost += (13 if chars <= 140 else 11) if bytes <= 160 else (7 if chars <= 140 else 0)
        return cost


if __name__ == "__main__":
    assert LengthLimitsOnMessagingPlatforms("test-input.txt").total_cost() == 31
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(LengthLimitsOnMessagingPlatforms(f"{input_folder}/i18n2025_day01.txt").total_cost())

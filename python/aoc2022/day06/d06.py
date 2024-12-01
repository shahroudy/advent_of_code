import os
from pathlib import Path
from myutils.io_handler import get_input_data


class TuningTrouble:
    def __init__(self, filename):
        self.stream = Path(filename).read_text().strip()

    def char_count(self, distinct_chars):
        for i in range(distinct_chars, len(self.stream)):
            if len(set(self.stream[i - distinct_chars : i])) == distinct_chars:
                return i


def test_samples(filename, answer1, answer2):
    test = TuningTrouble(filename)
    assert test.char_count(4) == answer1
    assert test.char_count(14) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 7, 19)

    tuning_trouble = TuningTrouble(data.input_file)
    print(tuning_trouble.char_count(4))
    print(tuning_trouble.char_count(14))

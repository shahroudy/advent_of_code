import os
from pathlib import Path


class StreamProcessing:
    def __init__(self, filename):
        self.line = Path(filename).read_text().strip()
        self.process()

    def process(self):
        depth = 0
        self.score = 0
        skip = False
        garbage = False
        self.garbage_count = 0
        for ch in self.line:
            if skip:
                skip = False
            elif ch == "!":
                skip = True
            elif ch == "<":
                if garbage:
                    self.garbage_count += 1
                garbage = True
            elif garbage:
                if ch == ">":
                    garbage = False
                else:
                    self.garbage_count += 1
            elif ch == "{":
                depth += 1
                self.score += depth
            elif ch == "}":
                depth -= 1

    def total_score(self):
        return self.score

    def non_cancelled_chars_in_garbage(self):
        return self.garbage_count


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = StreamProcessing(filename)
    assert test.total_score() == answer1 or answer1 is None
    assert test.non_cancelled_chars_in_garbage() == answer2 or answer2 is None


if __name__ == "__main__":
    test_samples("sample1.txt", 5, None)
    test_samples("sample2.txt", 16, None)
    test_samples("sample3.txt", 1, None)
    test_samples("sample4.txt", 9, None)
    test_samples("sample5.txt", 3, None)
    test_samples("sample6.txt", None, 10)

    print("Tests passed, starting with the puzzle")

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2017_day09.txt'
    puzzle = StreamProcessing(input_file)
    print(puzzle.total_score())
    print(puzzle.non_cancelled_chars_in_garbage())

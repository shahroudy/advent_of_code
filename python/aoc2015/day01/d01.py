from pathlib import Path

from myutils.io_handler import get_input_data


class NotQuiteLisp:
    def __init__(self, filename):
        self.enter_basement = -1
        self.current_floor = 0
        for i, c in enumerate(Path(filename).read_text().strip()):
            self.current_floor += 1 if c == "(" else -1
            if self.current_floor < 0 and self.enter_basement == -1:
                self.enter_basement = i + 1


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = NotQuiteLisp(filename)
    assert answer1 is None or test.current_floor == answer1
    assert answer2 is None or test.enter_basement == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 0, None)
    test_samples("sample2.txt", 3, None)
    test_samples("sample3.txt", -3, None)
    test_samples("sample4.txt", None, 1)
    test_samples("sample5.txt", None, 5)

    print("Tests passed, starting with the puzzle")

    puzzle = NotQuiteLisp(data.input_file)
    print(puzzle.current_floor)
    print(puzzle.enter_basement)

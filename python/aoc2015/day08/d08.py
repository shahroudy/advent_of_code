from pathlib import Path

from myutils.io_handler import get_input_data


class Matchsticks:
    def __init__(self, filename):
        self.input = Path(filename).read_text().splitlines()

    def extra_chars_from_string_literals(self):
        return sum(len(text) - len(eval(f"'{text[1:-1]}'")) for text in self.input)

    def extra_chars_from_encoding(self):
        return sum(2 + text.count("\\") + text.count('"') for text in self.input)


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = Matchsticks(filename)
    assert answer1 is None or test.extra_chars_from_string_literals() == answer1
    assert answer2 is None or test.extra_chars_from_encoding() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 12, 19)

    print("Tests passed, starting with the puzzle")

    puzzle = Matchsticks(data.input_file)

    print(puzzle.extra_chars_from_string_literals())
    print(puzzle.extra_chars_from_encoding())

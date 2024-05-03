import re
from json import loads
from pathlib import Path

from myutils.io_handler import get_input_data


class JSAbacusFrameworkIO:
    def __init__(self, filename):
        self.json = Path(filename).read_text().strip()

    def sum_all_ints(self):
        return sum(map(int, re.findall(r"-?\d+", self.json)))

    def sum_no_red_ints(self):
        def sum_values(node):
            if isinstance(node, int):
                return node
            if isinstance(node, list):
                return sum(sum_values(n) for n in node)
            if isinstance(node, dict):
                if "red" in node.values():
                    return 0
                return sum(sum_values(n) for n in node.values())
            return 0

        return sum_values(loads(self.json))


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = JSAbacusFrameworkIO(filename)
    assert answer1 is None or test.sum_all_ints() == answer1
    assert answer2 is None or test.sum_no_red_ints() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 6, 6)
    test_samples("sample2.txt", 6, None)
    test_samples("sample3.txt", 3, None)
    test_samples("sample4.txt", 3, None)
    test_samples("sample5.txt", 0, None)
    test_samples("sample6.txt", 0, None)
    test_samples("sample7.txt", 0, None)
    test_samples("sample8.txt", 0, None)
    test_samples("sample9.txt", None, 4)
    test_samples("sample10.txt", None, 0)
    test_samples("sample11.txt", None, 6)

    print("Tests passed, starting with the puzzle")

    puzzle = JSAbacusFrameworkIO(data.input_file)

    print(puzzle.sum_all_ints())
    print(puzzle.sum_no_red_ints())

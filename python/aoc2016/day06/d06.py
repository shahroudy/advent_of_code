from collections import Counter, defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class SignalsAndNoise:
    def __init__(self, filename):
        chars = defaultdict(list)
        for word in Path(filename).read_text().splitlines():
            for i, c in enumerate(word):
                chars[i].append(c)
        self.most_common = "".join([Counter(c).most_common()[0][0] for c in chars.values()])
        self.least_common = "".join([Counter(c).most_common()[-1][0] for c in chars.values()])


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = SignalsAndNoise("sample1.txt")
    assert test.most_common == "easter"
    assert test.least_common == "advent"

    print("Tests passed, starting with the puzzle")

    puzzle = SignalsAndNoise(data.input_file)

    print(puzzle.most_common)
    print(puzzle.least_common)

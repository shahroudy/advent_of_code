from collections import Counter
from datetime import UTC, datetime
from pathlib import Path


class Puzzle:
    def __init__(self, filename):
        self.times = Path(filename).read_text().splitlines()

    def calc(self):
        UTCs = [datetime.strptime(t, "%Y-%m-%dT%H:%M:%S%z").astimezone(UTC) for t in self.times]
        return Counter(UTCs).most_common(1)[0][0].strftime("%Y-%m-%dT%H:%M:%S%:z")


if __name__ == "__main__":

    assert Puzzle("test-input").calc() == "2019-06-05T12:15:00+00:00"

    print("Tests passed, starting with the puzzle")

    puzzle = Puzzle("input")

    print(puzzle.calc())

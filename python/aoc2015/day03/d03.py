from pathlib import Path

from myutils.io_handler import get_input_data


class PerfectlySphericalHousesInAVacuum:
    def __init__(self, filename):
        directions = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
        self.moves = [directions[ch] for ch in Path(filename).read_text().strip()]

    def visited_houses(self, moves):
        current = (0, 0)
        houses = {current}
        for move in moves:
            current = tuple(current[i] + move[i] for i in range(2))
            houses.add(current)
        return houses

    def visited_houses_santa_alone(self):
        return len(self.visited_houses(self.moves))

    def visited_houses_santa_and_robosanta(self):
        return len(self.visited_houses(self.moves[::2]) | self.visited_houses(self.moves[1::2]))


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = PerfectlySphericalHousesInAVacuum(filename)
    assert answer1 is None or test.visited_houses_santa_alone() == answer1
    assert answer2 is None or test.visited_houses_santa_and_robosanta() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 2, None)
    test_samples("sample2.txt", 4, 3)
    test_samples("sample3.txt", 2, 11)
    test_samples("sample4.txt", None, 3)

    print("Tests passed, starting with the puzzle")

    puzzle = PerfectlySphericalHousesInAVacuum(data.input_file)
    print(puzzle.visited_houses_santa_alone())
    print(puzzle.visited_houses_santa_and_robosanta())

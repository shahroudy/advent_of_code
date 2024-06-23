from pathlib import Path

from myutils.io_handler import get_input_data, submit_answer


class NoTimeforATaxicab:
    def __init__(self, filename):
        self.inp = [[c[0], int(c[1:])] for c in Path(filename).read_text().strip().split(", ")]

    def distance_of_final_position(self):
        x, y, dx, dy = 0, 0, 0, -1
        for dir, step in self.inp:
            if dir == "L":
                dx, dy = dy, -dx
            else:
                dx, dy = -dy, dx
            x += step * dx
            y += step * dy
        return abs(x) + abs(y)

    def distance_of_first_revisited_position(self):
        visited = set()
        x, y, dx, dy = 0, 0, 0, -1
        for dir, step in self.inp:
            if dir == "L":
                dx, dy = dy, -dx
            else:
                dx, dy = -dy, dx
            for _ in range(step):
                x += dx
                y += dy
                if (x, y) in visited:
                    return abs(x) + abs(y)
                else:
                    visited.add((x, y))


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = NoTimeforATaxicab(filename)
    assert answer1 is None or test.distance_of_final_position() == answer1
    assert answer2 is None or test.distance_of_first_revisited_position() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 5, None)
    test_samples("sample2.txt", 2, None)
    test_samples("sample3.txt", 12, None)
    test_samples("sample4.txt", None, 4)

    print("Tests passed, starting with the puzzle")

    puzzle = NoTimeforATaxicab(data.input_file)
    print(puzzle.distance_of_final_position())
    print(puzzle.distance_of_first_revisited_position())

from collections import defaultdict
from pathlib import Path

from myutils.geometry import MASK8, Point
from myutils.io_handler import get_input_data


class SeatingSystem:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()

        lines = self.input_text.splitlines()
        sets = defaultdict(set)
        for row, line in enumerate(lines):
            for col, ch in enumerate(line):
                if ch != ".":
                    sets[ch].add(Point(col, row))
        self.inp = dict(sets)
        self.rows, self.cols = row + 1, col + 1

    def occupied_seats_after_equilibrium(self, updated_rules=False):
        occupied_seats, empty_seats = self.inp.get("#", set()), self.inp.get("L", set())
        seats = occupied_seats | empty_seats
        neighbors = defaultdict(set)
        for seat in seats:
            for direction in MASK8:
                neighbor = seat + (vector := Point(*direction))
                while neighbor.is_inside(self):
                    if neighbor in seats:
                        neighbors[seat].add(neighbor)
                        break
                    if not updated_rules:
                        break
                    neighbor += vector
        equilibrium = False
        while not equilibrium:
            equilibrium = True
            new_occupied_seats, new_empty_seats = set(), set()
            for seat in seats:
                occupied_neighbors = sum(n in occupied_seats for n in neighbors[seat])
                if seat in empty_seats:
                    if occupied_neighbors == 0:
                        new_occupied_seats.add(seat)
                        equilibrium = False
                    else:
                        new_empty_seats.add(seat)
                else:
                    if occupied_neighbors >= (5 if updated_rules else 4):
                        new_empty_seats.add(seat)
                        equilibrium = False
                    else:
                        new_occupied_seats.add(seat)
            occupied_seats, empty_seats = new_occupied_seats, new_empty_seats
        return len(occupied_seats)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SeatingSystem("sample1.txt").occupied_seats_after_equilibrium(False) == 37
    assert SeatingSystem("sample1.txt").occupied_seats_after_equilibrium(True) == 26

    print("Tests passed, starting with the puzzle")

    puzzle = SeatingSystem(data.input_file)

    print(puzzle.occupied_seats_after_equilibrium(False))
    print(puzzle.occupied_seats_after_equilibrium(True))

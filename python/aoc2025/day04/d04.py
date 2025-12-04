from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import read_map_dict_of_sets_of_points


class PrintingDepartment:
    def __init__(self, filename):
        input_map, _, _ = read_map_dict_of_sets_of_points(Path(filename).read_text())
        self.rolls = input_map["@"]

    def number_of_accessible_rolls(self):
        return sum(sum(n in self.rolls for n in p.n8()) < 4 for p in self.rolls)

    def number_of_removed_rolls(self):
        rolls, removing = self.rolls.copy(), True
        while removing:
            rolls -= (removing := {p for p in rolls if sum(n in rolls for n in p.n8()) < 4})
        return len(self.rolls) - len(rolls)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert PrintingDepartment("sample1.txt").number_of_accessible_rolls() == 13
    assert PrintingDepartment("sample1.txt").number_of_removed_rolls() == 43

    print("Tests passed, starting with the puzzle")

    puzzle = PrintingDepartment(data.input_file)

    print(puzzle.number_of_accessible_rolls())
    print(puzzle.number_of_removed_rolls())

import re
from pathlib import Path

from myutils.io_handler import get_input_data


class MedicineForRudolph:
    def __init__(self, filename):
        replacements, self.medicine = Path(filename).read_text().split("\n\n")
        self.replacements = [re.findall(r"(\w+)", r) for r in replacements.splitlines()]

    def distinct_derivable_molecules(self):
        res = set()
        for left, right in self.replacements:
            for m in re.finditer(left, self.medicine):
                res.add(self.medicine[: m.start()] + right + self.medicine[m.end() :])
        return len(res)

    def min_steps_to_derive_the_medicine(self):
        replacements = sorted(self.replacements, key=lambda x: len(x[1]), reverse=True)
        count = 0
        medicine = self.medicine
        while medicine != "e":
            for left, right in replacements:
                if right in medicine:
                    medicine = medicine.replace(right, left, 1)
                    count += 1
                    break
        return count


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = MedicineForRudolph(filename)
    assert answer1 is None or test.distinct_derivable_molecules() == answer1
    assert answer2 is None or test.min_steps_to_derive_the_medicine() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 4, None)
    test_samples("sample2.txt", 7, None)
    test_samples("sample3.txt", None, 3)
    test_samples("sample4.txt", None, 6)

    print("Tests passed, starting with the puzzle")

    puzzle = MedicineForRudolph(data.input_file)

    print(puzzle.distinct_derivable_molecules())
    print(puzzle.min_steps_to_derive_the_medicine())

from itertools import permutations
from pathlib import Path

from myutils.io_handler import get_input_data


class Snailfish:
    def __init__(self, filename):
        self.snailfish = [eval(line) for line in Path(filename).read_text().splitlines()]

    def explode(self, snailfish, depth=0):
        """
        Returns:
            new_snailfish: list,
            value_to_be_added_left: int or None,
            value_to_be_added_right: int or None,
            exploded: bool
        """
        if isinstance(snailfish, int):
            return snailfish, None, None, False
        left, right = snailfish
        if depth == 4:
            return 0, left, right, True

        # check if the left side can explode
        new_left, num_to_add_left, num_to_add_right, exploded = self.explode(left, depth + 1)
        if exploded:
            new_right = self.add_number(right, num_to_add_right, to_left=True)
            return (new_left, new_right), num_to_add_left, None, True

        # check if the right side can explode
        new_right, num_to_add_left, num_to_add_right, exploded = self.explode(right, depth + 1)
        if exploded:
            new_left = self.add_number(left, num_to_add_left, to_left=False)
            return (new_left, new_right), None, num_to_add_right, True

        # no explosion available
        return snailfish, None, None, False

    def add_number(self, snailfish, value, to_left=True):
        if not value:
            return snailfish
        if isinstance(snailfish, int):
            return snailfish + value
        left, right = snailfish
        if to_left:
            return [self.add_number(left, value, to_left=True), right]
        else:
            return [left, self.add_number(right, value, to_left=False)]

    def split(self, snailfish):
        """
        Returns:
            new_snailfish: list,
            splitted: bool
        """
        if isinstance(snailfish, int):
            if snailfish >= 10:
                return [snailfish // 2, (snailfish + 1) // 2], True
            else:
                return snailfish, False

        left, right = snailfish

        # try to split the left side
        new_left, splitted = self.split(left)
        if splitted:
            return (new_left, right), True

        # try to split the right side
        new_right, splitted = self.split(right)
        if splitted:
            return [left, new_right], True

        # no split available
        return snailfish, False

    def reduce_snailfish(self, snailfish):
        while True:
            snailfish, _, _, exploded = self.explode(snailfish)
            if exploded:
                continue
            snailfish, splitted = self.split(snailfish)
            if splitted:
                continue
            return snailfish

    def magnitude(self, snailfish):
        if isinstance(snailfish, int):
            return snailfish
        left, right = snailfish
        return 3 * self.magnitude(left) + 2 * self.magnitude(right)

    def final_sum(self):
        snailfish = self.snailfish[0]
        for next_snailfish in self.snailfish[1:]:
            snailfish = self.reduce_snailfish([snailfish, next_snailfish])
        return self.magnitude(snailfish)

    def max_sum_of_pairs(self):
        return max(
            self.magnitude(self.reduce_snailfish([left, right]))
            for left, right in permutations(self.snailfish, 2)
        )


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = Snailfish("sample1.txt")
    assert test.final_sum() == 4140
    assert test.max_sum_of_pairs() == 3993

    print("Tests passed, starting with the puzzle")

    puzzle = Snailfish(data.input_file)

    print(puzzle.final_sum())
    print(puzzle.max_sum_of_pairs())

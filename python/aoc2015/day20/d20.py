from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class InfiniteElvesAndInfiniteHouses:
    def __init__(self, input=None):
        self.min_presents = (
            input if isinstance(input, int) else int(Path(input).read_text().strip())
        )

    def sum_of_divisors(self, house, infinite=True):
        result = 0
        for i in range(1, 1 + int(house**0.5)):
            if house % i == 0:
                j = house // i
                if infinite:
                    result += i
                    if j != i:
                        result += j
                else:
                    if i <= 50:
                        result += j
                    else:
                        break
        return result

    def lowest_house_number(self, deliver=10, infinite=True):
        min_presents = self.min_presents / deliver
        for house in count():
            if self.sum_of_divisors(house, infinite) >= min_presents:
                return house


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = InfiniteElvesAndInfiniteHouses(filename)
    assert answer1 is None or test.lowest_house_number(deliver=10, infinite=True) == answer1
    assert answer2 is None or test.lowest_house_number(deliver=11, infinite=False) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples(120, 6, None)
    test_samples(150, 8, None)
    test_samples(130, 8, None)

    print("Tests passed, starting with the puzzle")

    puzzle = InfiniteElvesAndInfiniteHouses(data.input_file)

    print(puzzle.lowest_house_number(deliver=10, infinite=True))
    print(puzzle.lowest_house_number(deliver=11, infinite=False))

from hashlib import md5
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class TheIdealStockingStuffer:
    def __init__(self, filename):
        self.secret_key = Path(filename).read_text().strip()

    def mine(self, zeroes=5):
        leading_zeros = "0" * zeroes
        for counter in count():
            code = (self.secret_key + str(counter)).encode()
            if md5(code).hexdigest().startswith(leading_zeros):
                return counter


def test_samples(filename, answer):
    test = TheIdealStockingStuffer(filename)
    assert test.mine() == answer


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 609043)
    test_samples("sample2.txt", 1048970)

    print("Tests passed, starting with the puzzle")

    puzzle = TheIdealStockingStuffer(data.input_file)
    print(puzzle.mine())
    print(puzzle.mine(zeroes=6))

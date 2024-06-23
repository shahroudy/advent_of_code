from hashlib import md5
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class HowAboutANiceGameOfChess:
    def __init__(self, filename):
        door_id = Path(filename).read_text().strip()
        password1, password2 = [], [0] * 8
        for counter in count():
            code = (door_id + str(counter)).encode()
            hash = md5(code).hexdigest()
            if md5(code).hexdigest().startswith("00000"):
                if len(password1) < 8:
                    password1.append(hash[5])
                if hash[5].isnumeric():
                    if (pos := int(hash[5])) < 8 and password2[pos] == 0:
                        password2[pos] = hash[6]
            if len(password1) == 8 and 0 not in password2:
                self.first_password = "".join(password1)
                self.second_password = "".join(password2)
                return


def test_samples(filename, answer1, answer2):
    test = HowAboutANiceGameOfChess(filename)
    assert test.first_password == answer1
    assert test.second_password == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", "18f47a30", "05ace8e3")

    print("Tests passed, starting with the puzzle")

    puzzle = HowAboutANiceGameOfChess(data.input_file)
    print(puzzle.first_password)
    print(puzzle.second_password)

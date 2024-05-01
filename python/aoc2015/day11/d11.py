from pathlib import Path

from myutils.io_handler import get_input_data


class CorporatePolicy:
    def __init__(self, filename=None, pwd=None):
        input = Path(filename).read_text().strip() if filename else pwd
        self.pwd = [ord(c) - ord("a") for c in input]
        self.val = {chr(i): i - ord("a") for i in range(ord("a"), ord("z") + 1)}

    def has_increasing_straight(self):
        for i in range(len(self.pwd) - 2):
            if self.pwd[i] + 1 == self.pwd[i + 1] and self.pwd[i] + 2 == self.pwd[i + 2]:
                return True
        return False

    def has_invalid_letters(self):
        return self.val["i"] in self.pwd or self.val["o"] in self.pwd or self.val["l"] in self.pwd

    def has_two_pairs(self):
        pair_count, i = 0, 0
        while i < len(self.pwd) - 1:
            if self.pwd[i] == self.pwd[i + 1]:
                pair_count += 1
                if pair_count == 2:
                    return True
                i += 2
            else:
                i += 1
        return False

    def is_valid_password(self):
        return (
            self.has_increasing_straight()
            and not self.has_invalid_letters()
            and self.has_two_pairs()
        )

    def increment(self):
        for i in range(len(self.pwd) - 1, -1, -1):
            if self.pwd[i] == self.val["z"]:
                self.pwd[i] = 0
            else:
                self.pwd[i] += 1
                break

    def get_password(self):
        return "".join(chr(c + ord("a")) for c in self.pwd)

    def find_next_valid_password(self):
        self.increment()
        while not self.is_valid_password():
            self.increment()
        return self.get_password()


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = CorporatePolicy(pwd="hijklmmn")
    assert test.has_increasing_straight()
    assert test.has_invalid_letters()

    test = CorporatePolicy(pwd="abbceffg")
    assert test.has_two_pairs()
    assert not test.has_increasing_straight()

    assert not CorporatePolicy(pwd="abbcegjk").has_two_pairs()

    assert CorporatePolicy(pwd="abcdefgh").find_next_valid_password() == "abcdffaa"
    assert CorporatePolicy(pwd="ghijklmn").find_next_valid_password() == "ghjaabcc"

    print("Tests passed, starting with the puzzle")

    puzzle = CorporatePolicy(data.input_file)

    print(puzzle.find_next_valid_password())
    print(puzzle.find_next_valid_password())

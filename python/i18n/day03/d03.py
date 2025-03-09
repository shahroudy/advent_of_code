from pathlib import Path


class Unicodepasswords:
    def __init__(self, filename):
        self.passwords = Path(filename).read_text().splitlines()

    def calc(self):
        return sum(
            4 <= len(password) <= 12
            and any(ch.isdigit() for ch in password)
            and any(ord(ch) >= 128 for ch in password)
            and any(ch.islower() for ch in password)
            and any(ch.isupper() for ch in password)
            for password in self.passwords
        )


if __name__ == "__main__":

    assert Unicodepasswords("test-input").calc() == 2

    print("Tests passed, starting with the puzzle")

    puzzle = Unicodepasswords("input")

    print(puzzle.calc())

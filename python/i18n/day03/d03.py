from pathlib import Path


class UnicodePasswords:
    def __init__(self, filename):
        self.passwords = Path(filename).read_text().splitlines()

    def count_valid_passwords(self):
        return sum(
            4 <= len(password) <= 12
            and any(ch.isdigit() for ch in password)
            and any(ord(ch) >= 128 for ch in password)
            and any(ch.islower() for ch in password)
            and any(ch.isupper() for ch in password)
            for password in self.passwords
        )


if __name__ == "__main__":
    assert UnicodePasswords("test-input").count_valid_passwords() == 2
    print("Tests passed, starting with the puzzle")
    print(UnicodePasswords("input").count_valid_passwords())

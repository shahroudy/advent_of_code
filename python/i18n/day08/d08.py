from collections import Counter
from pathlib import Path
from unicodedata import normalize


class UnicodePasswordsRedux:
    def __init__(self, filename):
        self.normalized_passwords = [
            normalize("NFD", line).encode("ascii", "ignore").decode("utf-8").lower()
            for line in Path(filename).read_text().splitlines()
        ]

    def count_valid_passwords(self):
        vowels = "aeiou"
        return sum(
            4 <= len(password) <= 12
            and any(c.isdigit() for c in password)
            and any(c in vowels for c in password)
            and any((c.isalpha() and (c not in vowels)) for c in password)
            and Counter(password).most_common(1)[0][1] == 1
            for password in self.normalized_passwords
        )


if __name__ == "__main__":
    assert UnicodePasswordsRedux("test-input").count_valid_passwords() == 2
    print("Tests passed, starting with the puzzle")
    print(UnicodePasswordsRedux("input").count_valid_passwords())

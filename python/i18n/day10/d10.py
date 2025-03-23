import concurrent.futures
import os
from functools import cache
from pathlib import Path
from unicodedata import normalize

import bcrypt


class UnicodePasswordsStrikeBack:
    def __init__(self, filename):
        encrypted_passwords, self.attempts = Path(filename).read_text().split("\n\n")
        self.passwords = {u: p for u, p in map(str.split, encrypted_passwords.splitlines())}

    @cache
    def accept(self, user, password):
        passwords = [""]
        for ch in password:
            if ord(ch) < 128:
                passwords = [p + ch for p in passwords]
            else:
                passwords = [p + ch for p in passwords] + [
                    p + normalize("NFD", ch) for p in passwords
                ]
        return any(bcrypt.checkpw(p.encode(), self.passwords[user].encode()) for p in passwords)

    def accept_line(self, line):
        user, password = line.split()
        return self.accept(user, normalize("NFC", password))

    def no_of_valid_attempts(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.accept_line, line) for line in self.attempts.splitlines()
            ]
        return sum(future.result() for future in futures)


if __name__ == "__main__":
    assert UnicodePasswordsStrikeBack("test-input.txt").no_of_valid_attempts() == 4
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(UnicodePasswordsStrikeBack(f"{input_folder}/i18n2025_day10.txt").no_of_valid_attempts())

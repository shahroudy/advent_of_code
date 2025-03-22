import re
from pathlib import Path


class GulliversPuzzleDictionary:
    def __init__(self, filename):
        self.codes, patterns = Path(filename).read_text().split("\n\n")
        self.regex = re.compile("|".join("^" + p.strip() + "$" for p in patterns.splitlines()))
        self.bom_and_encodings = [
            ("feff", "utf-16be"),
            ("fffe", "utf-16le"),
            ("efbbbf", "utf-8"),
            ("", "latin-1"),
            ("", "utf-8"),
            ("", "utf-16le"),
            ("", "utf-16be"),
        ]

    def solve(self):
        result = 0
        for row, code in enumerate(self.codes.splitlines()):
            for bom, encoding in self.bom_and_encodings:
                try:
                    if not code.startswith(bom):
                        continue
                    decoded = bytes.fromhex(code[len(bom) :]).decode(encoding)
                    if decoded.isalpha() and self.regex.match(decoded):
                        result += row + 1
                        continue
                except UnicodeDecodeError:
                    pass
        return result


if __name__ == "__main__":
    assert GulliversPuzzleDictionary("test-input").solve() == 47
    print("Tests passed, starting with the puzzle")
    print(GulliversPuzzleDictionary("input").solve())

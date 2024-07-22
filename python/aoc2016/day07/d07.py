import re
from pathlib import Path

from myutils.io_handler import get_input_data


class InternetProtocolVersion7:
    def __init__(self, filename):
        self.inp = [
            [re.sub(r"\[\w+\]", " ", s), " ".join(re.findall(r"\[(\w+)\]", s))]
            for s in Path(filename).read_text().splitlines()
        ]

    def is_ABBA(self, s):
        return bool(re.search(r"(?=(\w)(?!\1)(\w)\2\1)", s))

    def supports_TLS(self, s):
        return self.is_ABBA(s[0]) and not self.is_ABBA(s[1])

    def find_ABA(self, s):
        return set(re.findall(r"(?=(\w)(?!\1)(\w)\1)", s))

    def supports_SSL(self, s):
        in_abas, out_abas = self.find_ABA(s[0]), self.find_ABA(s[1])
        for aba in out_abas:
            if (aba[1], aba[0]) in in_abas:
                return True
        return False

    def TLS_count(self):
        return sum(self.supports_TLS(s) for s in self.inp)

    def SSL_count(self):
        return sum(self.supports_SSL(s) for s in self.inp)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert InternetProtocolVersion7("sample1.txt").TLS_count() == 2
    assert InternetProtocolVersion7("sample2.txt").SSL_count() == 3

    print("Tests passed, starting with the puzzle")

    puzzle = InternetProtocolVersion7(data.input_file)

    print(puzzle.TLS_count())
    print(puzzle.SSL_count())

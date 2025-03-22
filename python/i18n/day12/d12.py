import re
from pathlib import Path
from unicodedata import normalize


class SortingItOut:
    def __init__(self, filename: str):
        self.text = Path(filename).read_text().upper()

    def remove_accents(self, text: str):
        return normalize("NFD", text).encode("ascii", "ignore").decode("utf-8")

    def english(self, text):
        return self.remove_accents(text.replace("Æ", "AE").replace("Ø", "O"))

    def swedish(self, text: str):
        out = []
        for ch in text:
            if ch == "Æ":
                out.append("Ä")
            elif ch == "Ø":
                out.append("Ö")
            elif ch in "ÖÄÅ":
                out.append(ch)
            else:
                out.append(self.remove_accents(ch))
        return "".join(out)

    def dutch(self, text: str):
        return re.sub(r"VAN |DEN |DE |TEN |TER |TE ", "", self.english(text))

    def get_middle_number_in_sorted_list(self, text: str):
        info = re.findall(r"(.+), (.+): (.+)$", text, re.MULTILINE)
        info = [(re.sub(r"\W", "", t[0]), t[1], t[2]) for t in info]
        return int(sorted(info)[len(info) // 2][2])

    def product_of_three_middle_numbers(self):
        return (
            self.get_middle_number_in_sorted_list(self.english(self.text))
            * self.get_middle_number_in_sorted_list(self.swedish(self.text))
            * self.get_middle_number_in_sorted_list(self.dutch(self.text))
        )


if __name__ == "__main__":
    assert SortingItOut("test-input").product_of_three_middle_numbers() == 1885816494308838
    print("Tests passed, starting with the puzzle")
    print(SortingItOut("input").product_of_three_middle_numbers())

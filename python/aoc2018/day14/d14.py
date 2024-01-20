class ChocolateCharts:
    def __init__(self):
        self.init_recipes = "37"

    def calc1(self, after):
        recipes = self.init_recipes
        elf1, elf2 = 0, 1
        while len(recipes) < after + 10:
            e1, e2 = int(recipes[elf1]), int(recipes[elf2])
            recipes += str(e1 + e2)
            elf1 = (elf1 + e1 + 1) % len(recipes)
            elf2 = (elf2 + e2 + 1) % len(recipes)
        return recipes[after : after + 10]

    def calc2(self, pattern):
        recipes = self.init_recipes
        elf1, elf2 = 0, 1
        checked = 0
        while True:
            e1, e2 = int(recipes[elf1]), int(recipes[elf2])
            recipes += str(e1 + e2)
            elf1 = (elf1 + e1 + 1) % len(recipes)
            elf2 = (elf2 + e2 + 1) % len(recipes)
            while checked + len(pattern) <= len(recipes):
                if recipes[checked : checked + len(pattern)] == pattern:
                    return checked
                checked += 1


if __name__ == "__main__":
    test = ChocolateCharts()
    assert test.calc1(9) == "5158916779"
    assert test.calc1(5) == "0124515891"
    assert test.calc1(18) == "9251071085"
    assert test.calc1(2018) == "5941429882"
    assert test.calc2("51589") == 9
    assert test.calc2("01245") == 5
    assert test.calc2("92510") == 18
    assert test.calc2("59414") == 2018

    print("Tests passed, starting with the puzzle")

    puzzle = ChocolateCharts()
    print(puzzle.calc1(165061))
    print(puzzle.calc2("165061"))

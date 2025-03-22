from pathlib import Path


class DontStepInIt:
    def __init__(self, filename):
        park_map = Path(filename).read_text().splitlines()
        self.poop_loc = set()
        self.width, self.height = len(park_map[0]), len(park_map)
        for row, line in enumerate(park_map):
            for col, char in enumerate(line):
                if char == "💩":
                    self.poop_loc.add((col, row))

    def times_of_stepping_in_poo(self):
        return sum(((row * 2) % self.width, row) in self.poop_loc for row in range(self.height))


if __name__ == "__main__":
    assert DontStepInIt("test-input").times_of_stepping_in_poo() == 2
    print("Tests passed, starting with the puzzle")
    print(DontStepInIt("input").times_of_stepping_in_poo())

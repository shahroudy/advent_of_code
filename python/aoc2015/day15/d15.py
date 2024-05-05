import re
from pathlib import Path

from myutils.io_handler import get_input_data


class ScienceForHungryPeople:
    def __init__(self, filename):
        self.inp = [
            list(map(int, re.findall(r"-?\d+", line)))
            for line in Path(filename).read_text().splitlines()
        ]

    def find_highest_score_recipe(self, calories_goal=0):
        spoons = [0] * len(self.inp)
        highest_score = 0
        while spoons[0] <= 100:
            spoons[-1] = 100 - sum(spoons[:-1])
            if calories_goal > 0:
                calories = sum([spoons[i] * self.inp[i][-1] for i in range(len(spoons))])
            if not calories_goal or calories == calories_goal:
                score = 1
                for i in range(len(self.inp[0]) - 1):
                    score *= max(0, sum(spoons[j] * self.inp[j][i] for j in range(len(spoons))))
                    if score == 0:
                        break
                highest_score = max(highest_score, score)

            spoons[-2] += 1
            for i in range(len(spoons) - 2, 0, -1):
                if sum(spoons[:-1]) > 100:
                    spoons[i] = 0
                    spoons[i - 1] += 1
                else:
                    break
        return highest_score


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = ScienceForHungryPeople("sample1.txt")
    assert test.find_highest_score_recipe() == 62842880
    assert test.find_highest_score_recipe(calories_goal=500) == 57600000

    print("Tests passed, starting with the puzzle")

    puzzle = ScienceForHungryPeople(data.input_file)

    print(puzzle.find_highest_score_recipe())
    print(puzzle.find_highest_score_recipe(calories_goal=500))

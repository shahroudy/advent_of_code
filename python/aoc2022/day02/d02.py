import os
from pathlib import Path


class RockPaperScissors:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.games = [(ord(g[0]) - ord("A"), ord(g[2]) - ord("X")) for g in self.lines]

    def total_score_first_strategy(self):
        score = 0
        for game in self.games:
            op_move, my_move = game
            round_score = ((my_move - op_move + 1) % 3) * 3
            move_score = 1 + my_move
            score += round_score + move_score
        return score

    def total_score_second_strategy(self):
        score = 0
        for game in self.games:
            op_move, result = game
            my_move = (op_move + result - 1) % 3
            round_score = result * 3
            move_score = 1 + my_move
            score += round_score + move_score
        return score


def test_samples(filename, answer1, answer2):
    test = RockPaperScissors(filename)
    assert test.total_score_first_strategy() == answer1
    assert test.total_score_second_strategy() == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", 15, 12)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day02.txt'
    rock_paper_scissors = RockPaperScissors(input_file)
    print(rock_paper_scissors.total_score_first_strategy())
    print(rock_paper_scissors.total_score_second_strategy())

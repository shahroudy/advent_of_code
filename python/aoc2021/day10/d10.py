import os
from myutils.file_reader import read_lines


class SyntaxScoring:
    def __init__(self, filename):
        self.lines = read_lines(filename)

    def find_scores(self):
        syntax_error_score = 0
        incomplete_scores = []
        illegal_points = {")": 3, "]": 57, r"}": 1197, ">": 25137}
        incomplete_points = {"(": 1, "[": 2, r"{": 3, "<": 4}

        for line in self.lines:
            stack = list()
            for ch in line:
                if ch in "([{<":
                    stack.append(ch)
                else:
                    o = stack.pop()
                    if o + ch in ["()", "[]", r"{}", "<>"]:
                        continue
                    else:
                        syntax_error_score += illegal_points[ch]
                        stack.clear()
                        break
            else:
                incomplete_score = 0
                while stack:
                    o = stack.pop()
                    incomplete_score = incomplete_score * 5 + incomplete_points[o]
                incomplete_scores.append(incomplete_score)
        incomplete_scores.sort()
        return (
            syntax_error_score,
            incomplete_scores[len(incomplete_scores) // 2],
        )


if __name__ == "__main__":
    test1 = SyntaxScoring("test1.txt")
    assert test1.find_scores() == (26397, 288957)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2021_day10.txt'
    syntax_scoring = SyntaxScoring(input_file)
    print(syntax_scoring.find_scores())

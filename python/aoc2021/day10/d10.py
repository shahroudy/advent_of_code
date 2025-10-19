from pathlib import Path

from myutils.io_handler import get_input_data


class SyntaxScoring:
    def __init__(self, filename):
        self.illegal_chars, self.incomplete_stacks = [], []
        self._process_lines(Path(filename).read_text().splitlines())

    def _process_lines(self, lines):
        for line in lines:
            self._process_line(line)

    def _process_line(self, line):
        stack = []
        closing = {"(": ")", "[": "]", "{": "}", "<": ">"}
        for current_char in line:
            if current_char in closing.keys():
                stack.append(current_char)
            else:
                if not stack or current_char != closing[stack.pop()]:
                    self.illegal_chars.append(current_char)
                    return
        self.incomplete_stacks.append(stack)

    def _get_stack_score(self, stack):
        points = {"(": 1, "[": 2, "{": 3, "<": 4}
        return sum(points[character] * (5**index) for index, character in enumerate(stack))

    def total_syntax_error_score(self):
        error_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        return sum(error_points[illegal_char] for illegal_char in self.illegal_chars)

    def middle_incomplete_score(self):
        scores = sorted([self._get_stack_score(stack) for stack in self.incomplete_stacks])
        return scores[len(scores) // 2]


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SyntaxScoring("sample1.txt").total_syntax_error_score() == 26397
    assert SyntaxScoring("sample1.txt").middle_incomplete_score() == 288957

    print("Tests passed, starting with the puzzle")

    puzzle = SyntaxScoring(data.input_file)

    print(puzzle.total_syntax_error_score())
    print(puzzle.middle_incomplete_score())

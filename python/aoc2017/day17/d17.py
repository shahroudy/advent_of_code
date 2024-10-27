from collections import deque
from pathlib import Path

from myutils.io_handler import get_input_data


class Spinlock:
    def __init__(self, input):
        self.steps_forward = int(Path(input).read_text()) if isinstance(input, str) else input

    def value_after_2017(self):
        q = deque([0])
        for i in range(1, 2018):
            q.rotate(-self.steps_forward)
            q.append(i)
        return q[0]

    def value_after_0_on_50_million_steps(self):
        current = 0
        for i in range(1, 50000001):
            current = (current + self.steps_forward) % i
            if current == 0:
                result = i
            current += 1
        return result


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert Spinlock(3).value_after_2017() == 638

    print("Tests passed, starting with the puzzle")

    puzzle = Spinlock(data.input_file)
    print(puzzle.value_after_2017())
    print(puzzle.value_after_0_on_50_million_steps())

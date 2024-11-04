import re
from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class TheHaltingProblem:
    def __init__(self, filename):
        input = Path(filename).read_text()

        self.init_state = re.search(r"Begin in state (\w).", input).group(1)
        self.steps = int(re.search(r"diagnostic checksum after (\d+) steps.", input).group(1))
        rule_re = re.compile(
            r"""In state (\w):
  If the current value is 0:
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w).
  If the current value is 1:
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w)."""
        )
        self.inp = {match[0]: match[1:] for match in re.findall(rule_re, input)}

    def diagnostic_checksum(self):
        state = self.init_state
        tape = defaultdict(int)
        head = 0
        for _ in range(self.steps):
            value = tape[head]
            output, move, next = self.inp[state][value * 3 : value * 3 + 3]
            tape[head] = int(output)
            head += 1 if move == "right" else -1
            state = next
        return sum(tape.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TheHaltingProblem("sample1.txt").diagnostic_checksum() == 3

    print("Tests passed, starting with the puzzle")

    puzzle = TheHaltingProblem(data.input_file)

    print(puzzle.diagnostic_checksum())

import os
from pathlib import Path


class RexToLynx:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().splitlines()

    def rex(self, line):
        return int(round(eval("".join(ch for ch in line if ord(ch) < 128))))

    def lynx(self, line):
        current = []
        level = 0
        left_to_right = True
        for char in line:
            if char == "\u2067":  # RLI
                if left_to_right:
                    level += 1
                    left_to_right = False
            elif char == "\u2066":  # LRI
                if not left_to_right:
                    level += 1
                    left_to_right = True
            elif char == "\u2069":  # PDI
                level -= 1
                left_to_right = not left_to_right
            elif char.isnumeric():
                current.append((char, level + level % 2))
            elif char in "()" and not left_to_right:
                current.append((")" if char == "(" else "(", level))
            else:
                current.append((char, level))
        while max_embedding_level := max(embedding_level for _, embedding_level in current) > 0:
            next = []
            stack = []
            for char, embedding_level in current:
                if embedding_level < max_embedding_level:
                    while stack:
                        next.append(stack.pop())
                    next.append((char, embedding_level))
                else:
                    stack.append((char, embedding_level - 1))
            while stack:
                next.append(stack.pop())
            current = next
        return int(round(eval("".join(char for char, _ in current))))

    def sum_of_differences(self):
        return sum(abs(self.rex(line) - self.lynx(line)) for line in self.lines)


if __name__ == "__main__":
    assert RexToLynx("test-input.txt").sum_of_differences() == 19282
    print("Tests passed, starting with the puzzle")
    input_folder = os.environ.get("i18n_inputs")
    print(RexToLynx(f"{input_folder}/i18n2025_day18.txt").sum_of_differences())

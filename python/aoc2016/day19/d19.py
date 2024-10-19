from pathlib import Path

from myutils.io_handler import get_input_data


class AnElephantNamedJoseph:
    def __init__(self, input):
        self.elf_count = input if isinstance(input, int) else int(Path(input).read_text().strip())

    def who_wins_grab_from_left(self):
        next = {i: i + 1 for i in range(1, self.elf_count)}
        next[self.elf_count] = 1
        current = 1
        while True:
            next[current] = next[next[current]]
            if current == next[current]:
                return current
            current = next[current]

    def who_wins_grab_from_front_ad_hoc(self, elf_count=None):
        elf_count = elf_count or self.elf_count
        next = {i: i + 1 for i in range(1, elf_count)}
        next[elf_count] = 1
        current = 1
        remaining_elf_count = elf_count
        while True:
            if next[current] == current:
                return current
            distance = remaining_elf_count // 2 - 1
            grab_from = current
            for _ in range(distance):
                grab_from = next[grab_from]
            next[grab_from] = next[next[grab_from]]
            current = next[current]
            remaining_elf_count -= 1

    def who_wins_grab_from_front(self):
        winner = 1
        for i in range(2, self.elf_count + 1):
            if winner == i - 1:
                winner = 1
            elif winner >= i // 2:
                winner += 2
            else:
                winner += 1
        return winner


def test_samples(input, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = AnElephantNamedJoseph(input)
    assert answer1 is None or test.who_wins_grab_from_left() == answer1
    assert answer2 is None or test.who_wins_grab_from_front() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples(5, 3, 2)
    test_samples(20, None, 13)
    test_samples(100, None, 19)
    test_samples(200, None, 157)
    test_samples(999, None, 270)

    print("Tests passed, starting with the puzzle")

    puzzle = AnElephantNamedJoseph(data.input_file)

    print(puzzle.who_wins_grab_from_left())
    print(puzzle.who_wins_grab_from_front())

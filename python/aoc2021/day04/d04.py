from functools import reduce
from pathlib import Path

from myutils.io_handler import get_input_data


class GiantSquid:
    def __init__(self, filename):
        text = Path(filename).read_text().split("\n\n")
        self.numbers = list(map(int, text[0].split(",")))
        self.boards = [[list(map(int, r.split())) for r in b.splitlines()] for b in text[1:]]

    def bingo_board(self, board, read_numbers):
        return any(all(n in read_numbers for n in row) for row in board) or any(
            all(row[col] in read_numbers for row in board) for col in range(len(board[0]))
        )

    def sum_of_unmarked(self, board, read_numbers):
        return sum(set(reduce(lambda x, y: x + y, board)) - read_numbers)

    def first_winning_board_score(self):
        read_numbers = set()
        for n in self.numbers:
            read_numbers.add(n)
            for board in self.boards:
                if self.bingo_board(board, read_numbers):
                    return n * self.sum_of_unmarked(board, read_numbers)

    def last_winning_board_score(self):
        read_numbers = set()
        remaining_boards = set(range(len(self.boards)))
        for n in self.numbers:
            read_numbers.add(n)
            for board_index in remaining_boards.copy():
                board = self.boards[board_index]
                if self.bingo_board(board, read_numbers):
                    remaining_boards.remove(board_index)
                    if not remaining_boards:
                        return n * self.sum_of_unmarked(board, read_numbers)


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert GiantSquid("sample1.txt").first_winning_board_score() == 4512
    assert GiantSquid("sample1.txt").last_winning_board_score() == 1924

    print("Tests passed, starting with the puzzle")

    puzzle = GiantSquid(data.input_file)

    print(puzzle.first_winning_board_score())
    print(puzzle.last_winning_board_score())

import os
from pathlib import Path
from myutils.io_handler import get_input_data


class PyroclasticFlow:
    def __init__(self, filename):
        self.moves = [-1 if c == "<" else 1 for c in Path(filename).read_text().strip()]
        self.rock_patters = {
            0: ((2, 4), (3, 4), (4, 4), (5, 4)),  # --
            1: ((3, 4), (2, 5), (3, 5), (4, 5), (3, 6)),  # +
            2: ((2, 4), (3, 4), (4, 4), (4, 5), (4, 6)),  # L
            3: ((2, 4), (2, 5), (2, 6), (2, 7)),  # |
            4: ((2, 4), (3, 4), (2, 5), (3, 5)),  # #
        }

    def reset(self):
        self.board = set()
        self.rock_head = 0
        self.max_height = 0
        self.input_head = 0

    def put_new_rock(self):
        self.rock = {(r[0], r[1] + self.max_height) for r in self.rock_patters[self.rock_head]}
        self.rock_head += 1
        if self.rock_head == 5:
            self.rock_head = 0

    def get_move(self):
        move = self.moves[self.input_head]
        self.input_head += 1
        if self.input_head == len(self.moves):
            self.input_head = 0
        return move

    def print_board(self):
        print()
        for height in range(self.max_height + 6, self.max_height - 10, -1):
            if height == 0:
                print("=========")
                break
            print("|", end="")
            for col in range(7):
                point = (col, height)
                print("@" if point in self.rock else "#" if point in self.board else ".", end="")
            print("|")
        print()

    def move_rock_one_step(self):
        move = self.get_move()
        moved_rock = set()
        for point in self.rock:
            if 0 <= point[0] + move < 7 and (point[0] + move, point[1]) not in self.board:
                moved_rock.add((point[0] + move, point[1]))
            else:
                moved_rock = self.rock.copy()
                break
        self.rock = moved_rock

        moving_down = True
        for point in self.rock:
            if point[1] == 1 or (point[0], point[1] - 1) in self.board:
                moving_down = False
                break
        if not moving_down:
            for point in self.rock:
                self.board.add(point)
                self.max_height = max(self.max_height, point[1])
        else:
            moved_rock = set()
            for point in self.rock:
                moved_rock.add((point[0], point[1] - 1))
            self.rock = moved_rock
        return moving_down

    def rock_zero_is_blocked(self):
        if self.rock_head != 0:
            return False
        horizontal_gap = 0
        for col in [(i, self.max_height) in self.board for i in range(7)]:
            if col:
                horizontal_gap = 0
            else:
                horizontal_gap += 1
            if horizontal_gap == 4:
                return False
        return True

    def calc_height_after(self, iterations, visualize=False):
        self.reset()
        patterns = dict()
        fast_forwarded = False
        fast_forwarded_height = 0
        iter = 0
        while iter < iterations:
            if (not fast_forwarded) and self.rock_zero_is_blocked():
                if self.input_head in patterns:
                    pre_iter, pre_height = patterns[self.input_head]
                    delta_iter = iter - pre_iter
                    delta_height = self.max_height - pre_height
                    fast_forward_count = (iterations - iter) // delta_iter
                    iter += delta_iter * fast_forward_count
                    fast_forwarded_height += fast_forward_count * delta_height
                    fast_forwarded = True
                else:
                    patterns[self.input_head] = (iter, self.max_height)
            self.put_new_rock()
            while self.move_rock_one_step():
                if visualize:
                    self.print_board()
            iter += 1
        return self.max_height + fast_forwarded_height


def test_samples(filename, answer1, answer2):
    test = PyroclasticFlow(filename)
    assert test.calc_height_after(2022) == answer1
    assert test.calc_height_after(1000000000000) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 3068, 1514285714288)

    pyroclastic_flow = PyroclasticFlow(data.input_file)
    print(pyroclastic_flow.calc_height_after(2022))
    print(pyroclastic_flow.calc_height_after(1000000000000))

import os
from collections import deque
from myutils.file_reader import read_lines
from myutils.io_handler import get_input_data


class Chiton:
    def __init__(self, filename):
        self.lines = read_lines(filename)
        self.mask4 = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1]]
        self.process_num_map()

    def process_num_map(self):
        self.map = dict()
        row = 0
        for line in self.lines:
            col = 0
            for ch in line:
                self.map[(row, col)] = int(ch)
                col += 1
            if row == 0:
                self.cols = col
            col = 0
            row += 1
        self.rows = row

    def replicate_map(self):
        new_map = self.map.copy()
        for i in range(0, 5):
            for j in range(0, 5):
                if i == 0 and j == 0:
                    continue
                for x, y in self.map.keys():
                    xn, yn = (x + j * self.cols, y + i * self.rows)
                    new_point = (xn, yn)
                    ref_point = (xn - self.cols, yn)
                    if ref_point[0] < 0:
                        ref_point = (xn, yn - self.rows)
                    new_map[new_point] = new_map[ref_point] + 1
                    if new_map[new_point] > 9:
                        new_map[new_point] = 1
        self.map = new_map
        self.cols = self.cols * 5
        self.rows = self.rows * 5

    def lowest_total_risk(self, replicate=False):
        if replicate:
            self.replicate_map()
        start = (0, 0)
        queue = deque()
        queue.append(start)
        risk = dict()
        risk[start] = 0
        while queue:
            point = queue.popleft()
            for dir in self.mask4:
                neighbor = (point[0] + dir[0], point[1] + dir[1])
                if neighbor in self.map:
                    neighbor_risk = risk[point] + self.map[neighbor]
                    if neighbor not in risk or risk[neighbor] > neighbor_risk:
                        queue.append(neighbor)
                        risk[neighbor] = neighbor_risk
        return risk[(self.cols - 1, self.rows - 1)]


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = Chiton("test1.txt")
    assert test1.lowest_total_risk(False) == 40
    assert test1.lowest_total_risk(True) == 315

    chiton = Chiton(data.input_file)
    print(chiton.lowest_total_risk(False))
    print(chiton.lowest_total_risk(True))

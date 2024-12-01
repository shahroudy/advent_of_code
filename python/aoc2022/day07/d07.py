import os
from collections import defaultdict
from pathlib import Path
from myutils.io_handler import get_input_data


class NoSpaceLeftOnDevice:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        self.dir = defaultdict(list)
        self.sizes = defaultdict(int)
        read_mode = False
        for line in self.lines:
            if read_mode:
                if line[0] == "$":
                    read_mode = False
                else:
                    parts = line.split()
                    if parts[0] == "dir":
                        self.dir[tuple(current)].append(parts[1])
                        self.dir[tuple(current + [parts[1]])] = []
                    else:
                        self.sizes[tuple(current + [parts[1]])] = int(parts[0])
                        parent = current.copy()
                        while parent:
                            self.sizes[tuple(parent)] += int(parts[0])
                            parent.pop()
            if not read_mode:
                if line == "$ cd /":
                    current = ["/"]
                elif line == "$ cd ..":
                    current.pop()
                elif line[:5] == "$ cd ":
                    current.append(line[5:])
                elif line == "$ ls":
                    read_mode = True

    def sum_of_all_small_dirs(self):
        return sum([self.sizes[dir] for dir in self.dir if self.sizes[dir] <= 100000])

    def min_dir_size_to_delete(self):
        needed_space = 30000000 - (70000000 - self.sizes[tuple("/")])
        return min([self.sizes[dir] for dir in self.dir if self.sizes[dir] >= needed_space])


def test_samples(filename, answer1, answer2):
    test = NoSpaceLeftOnDevice(filename)
    assert test.sum_of_all_small_dirs() == answer1
    assert test.min_dir_size_to_delete() == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    test_samples("sample1.txt", 95437, 24933642)

    no_space_left_on_device = NoSpaceLeftOnDevice(data.input_file)
    print(no_space_left_on_device.sum_of_all_small_dirs())
    print(no_space_left_on_device.min_dir_size_to_delete())

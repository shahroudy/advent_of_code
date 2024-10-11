import re
from collections import defaultdict, deque
from hashlib import md5
from multiprocessing import Pool
from pathlib import Path

from myutils.io_handler import get_input_data


class OneTimePad:
    def __init__(self, filename):
        self.salt = Path(filename).read_text().strip()
        self.re3 = re.compile(r"(.)\1\1")
        self.re5 = re.compile(r"(.)\1\1\1\1")

    def reset(self):
        self.threes = deque()
        self.fives = defaultdict(deque)
        self.processed = 0

    def get_reps(self, index):
        three = None
        fives = []
        hash = self.salt + str(index)
        for _ in range(self.hash_repeat):
            hash = md5(hash.encode()).hexdigest()
        if match := self.re3.search(hash):
            three = match.group(1)
            for match in re.findall(self.re5, hash):
                fives.append(match)
        return index, three, fives

    def process_indices(self):
        batch = 5000
        workers = 32
        with Pool(workers) as p:
            outputs = p.map(self.get_reps, range(self.processed, self.processed + batch))
        for index, three, five in outputs:
            if three:
                self.threes.append((index, three))
                for f in five:
                    self.fives[f].append(index)
        self.processed += batch

    def find_64th_key(self, hash_repeat=0):
        self.hash_repeat = hash_repeat + 1
        self.reset()
        key_count = 0
        while True:
            while not self.threes:
                self.process_indices()
            index, character = self.threes.popleft()
            last_index = index + 1000
            while last_index >= self.processed:
                self.process_indices()
            while self.fives[character] and (self.fives[character][0] <= index):
                self.fives[character].popleft()
            if self.fives[character] and (self.fives[character][0] <= last_index):
                key_count += 1
                if key_count == 64:
                    return index


def test_samples(filename, answer1, answer2):
    if answer1 is None and answer2 is None:
        return
    test = OneTimePad(filename)
    assert answer1 is None or test.find_64th_key() == answer1
    assert answer2 is None or test.find_64th_key(2016) == answer2


if __name__ == "__main__":
    data = get_input_data(__file__)

    from time import time

    t = time()
    test_samples("sample1.txt", 22728, 22551)

    print("Tests passed, starting with the puzzle")

    puzzle = OneTimePad(data.input_file)

    print(puzzle.find_64th_key())
    print(puzzle.find_64th_key(2016))

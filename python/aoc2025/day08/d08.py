from itertools import combinations
from pathlib import Path

from myutils.io_handler import get_input_data


class Playground:
    def __init__(self, filename, observe_at_step):
        boxes = [list(map(int, box.split(","))) for box in Path(filename).read_text().splitlines()]
        distances = {
            sum((a - b) ** 2 for a, b in zip(boxes[p], boxes[q])): (p, q)
            for p, q in combinations(range(len(boxes)), 2)
        }
        connected_boxes = {box: {box} for box in range(len(boxes))}
        for iteration, distance in enumerate(sorted(distances)):
            if iteration == observe_at_step:
                circuits = {tuple(sorted(connected)) for connected in connected_boxes.values()}
                sizes = sorted([len(c) for c in circuits], reverse=True)
                self.three_largest_sizes = sizes[0] * sizes[1] * sizes[2]
            p, q = distances[distance]
            if p not in connected_boxes[q]:
                new_circuit = connected_boxes[p] | connected_boxes[q]
                for box in new_circuit:
                    connected_boxes[box] = new_circuit
                if len(new_circuit) == len(boxes):
                    self.last_connection = boxes[q][0] * boxes[p][0]
                    break


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = Playground("sample1.txt", observe_at_step=10)
    assert test.three_largest_sizes == 40
    assert test.last_connection == 25272

    print("Tests passed, starting with the puzzle")

    puzzle = Playground(data.input_file, observe_at_step=1000)

    print(puzzle.three_largest_sizes)
    print(puzzle.last_connection)

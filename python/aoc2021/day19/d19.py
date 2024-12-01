import os
import numpy as np
from collections import defaultdict
from myutils.file_reader import read_line_groups
from time import time

rot24 = np.array(
    [
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
        [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
        [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
        [[0, 0, 1], [1, 0, 0], [0, 1, 0]],
        [[0, 1, 0], [1, 0, 0], [0, 0, -1]],
        [[0, 0, -1], [1, 0, 0], [0, -1, 0]],
        [[-1, 0, 0], [0, -1, 0], [0, 0, 1]],
        [[-1, 0, 0], [0, 0, -1], [0, -1, 0]],
        [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
        [[-1, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
        [[0, 0, 1], [-1, 0, 0], [0, -1, 0]],
        [[0, -1, 0], [-1, 0, 0], [0, 0, -1]],
        [[0, 0, -1], [-1, 0, 0], [0, 1, 0]],
        [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
        [[0, 1, 0], [0, 0, 1], [1, 0, 0]],
        [[0, 0, 1], [0, -1, 0], [1, 0, 0]],
        [[0, -1, 0], [0, 0, -1], [1, 0, 0]],
        [[0, 0, -1], [0, -1, 0], [-1, 0, 0]],
        [[0, -1, 0], [0, 0, 1], [-1, 0, 0]],
        [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
        [[0, 1, 0], [0, 0, -1], [-1, 0, 0]],
    ]
)
from myutils.io_handler import get_input_data


class BeaconScanner:
    def __init__(self, filename):
        self.line_groups = read_line_groups(filename)
        self.process()

    def process(self):
        self.detections = []
        self.scanner_count = 0
        for lg in self.line_groups:
            det = []
            for line in lg[1:]:
                coor = line.split(",")
                coor = list(map(int, coor))
                det.append(coor)
            self.detections.append(np.array(det))
            self.scanner_count += 1

    def set_pairwise_beacon_distances(self):
        self.pairwise_beacon_distances = defaultdict(list)
        for scanner in range(self.scanner_count):
            detections = self.detections[scanner]
            for i in range(len(detections)):
                dists = set()
                for j in range(len(detections)):
                    if j != i:
                        d = np.sum((detections[i] - detections[j]) ** 2)
                        dists.add(d)
                assert len(dists) == len(detections) - 1
                self.pairwise_beacon_distances[scanner].append(dists)

    def align_scanner_pair(self, ref_scanner, cur_scanner):
        ref_detections = self.detections[ref_scanner]
        cur_detections = self.detections[cur_scanner]
        match = self.matching_beacons[(ref_scanner, cur_scanner)]

        for rotation in rot24:
            transformed = np.dot(cur_detections, rotation)
            frompoint = transformed[match[0][0]]
            topoint = ref_detections[match[0][1]]
            delta = topoint - frompoint
            transformed = transformed + delta

            for mc, mr in match:
                if np.sum(np.abs(transformed[mc] - ref_detections[mr])) > 0:
                    break  # not the correct rotation
            else:  # found
                self.detections[cur_scanner] = transformed
                self.scanner_coordinations[cur_scanner] = delta
                return

    def find_matched_beacons(self, ref_scanner, cur_scanner):
        ref_distances = self.pairwise_beacon_distances[ref_scanner]
        cur_distances = self.pairwise_beacon_distances[cur_scanner]

        match = []
        for i in range(len(cur_distances)):
            for j in range(len(ref_distances)):
                if len(cur_distances[i] & ref_distances[j]) == 11:
                    match.append([i, j])
                    break
        return match

    def find_matching_scanners(self):
        self.matching_scanners = defaultdict(list)
        self.matching_beacons = {}
        for i in range(self.scanner_count):
            for j in range(i, self.scanner_count):
                match = self.find_matched_beacons(i, j)
                if len(match) < 12:
                    continue
                self.matching_scanners[i].append(j)
                self.matching_scanners[j].append(i)
                self.matching_beacons[(i, j)] = match
                self.matching_beacons[(j, i)] = [(y, x) for (x, y) in match]

    def count_all_beacons(self):
        beacons = set()
        for d in self.detections:
            for p in d:
                beacons.add(tuple((p[0], p[1], p[2])))
        return len(beacons)

    def max_distance_between_scanners(self):
        max_distance = 0
        for i in self.scanner_coordinations.values():
            for j in self.scanner_coordinations.values():
                max_distance = max(max_distance, np.sum(np.abs(i - j)))
        return max_distance

    def align_all_scanners(self):
        self.set_pairwise_beacon_distances()
        self.find_matching_scanners()

        self.scanner_coordinations = {0: np.array([0, 0, 0])}
        matched = {0}
        queue = [0]
        while queue:
            ref_scanner = queue.pop()
            for cur_scanner in self.matching_scanners[ref_scanner]:
                if cur_scanner not in matched:
                    self.align_scanner_pair(ref_scanner, cur_scanner)
                    queue.append(cur_scanner)
                    matched.add(cur_scanner)

        return (self.count_all_beacons(), self.max_distance_between_scanners())


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = BeaconScanner("test1.txt")
    assert test1.align_all_scanners() == (79, 3621)
    beacon_scanner = BeaconScanner(data.input_file)
    print(beacon_scanner.align_all_scanners())

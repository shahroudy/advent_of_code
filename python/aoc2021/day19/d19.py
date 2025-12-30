from dataclasses import dataclass, field
from itertools import combinations, product
from pathlib import Path

from myutils.geometry import Point3D
from myutils.io_handler import get_input_data
from myutils.optimization import apply_transformation, find_Nd_to_Nd_transformation


@dataclass
class Beacon:
    position: Point3D
    distances: set[int] = field(default_factory=set)
    matches: dict[int, "Beacon"] = field(default_factory=dict)
    real_position: Point3D | None = None


@dataclass
class Scanner:
    id: int
    beacons: list[Beacon]
    overlapping_scanners: set[int] = field(default_factory=set)
    position: Point3D | None = None


class BeaconScanner:
    def __init__(self, filename):
        self.scanners = self.load_scanners(filename)
        self.set_pairwise_beacon_distances()
        self.find_matching_scanners()
        self.find_scanners_and_beacons_positions()

    def load_scanners(self, filename):
        scanners = []
        for id, scanner in enumerate(Path(filename).read_text().split("\n\n")):
            beacons = [
                Beacon(position=Point3D(*map(int, beacon.split(","))))
                for beacon in scanner.splitlines()[1:]
            ]
            scanners.append(Scanner(id=id, beacons=beacons))
        return scanners

    def set_pairwise_beacon_distances(self):
        for scanner in self.scanners:
            for beacon1, beacon2 in combinations(scanner.beacons, 2):
                distance = beacon1.position.distance_squared(beacon2.position)
                beacon1.distances.add(distance)
                beacon2.distances.add(distance)

    def find_matching_scanners(self):
        for scanner1, scanner2 in combinations(self.scanners, 2):
            s1_id, s2_id = scanner1.id, scanner2.id
            beacon_match_count = 0
            for beacon1, beacon2 in product(scanner1.beacons, scanner2.beacons):
                if len(beacon1.distances & beacon2.distances) >= 11:
                    beacon_match_count += 1
                    beacon1.matches[s2_id] = beacon2
                    beacon2.matches[s1_id] = beacon1
            if beacon_match_count >= 12:
                scanner1.overlapping_scanners.add(s2_id)
                scanner2.overlapping_scanners.add(s1_id)

    def find_scanners_and_beacons_positions(self):
        for beacon in self.scanners[0].beacons:
            beacon.real_position = beacon.position
        self.scanners[0].position = Point3D(0, 0, 0)
        matched = {0}
        to_be_matched = [0]
        while to_be_matched:
            ref_scanner = self.scanners[to_be_matched.pop()]
            for cur_scanner_id in ref_scanner.overlapping_scanners - matched:
                cur_scanner = self.scanners[cur_scanner_id]
                self.align_scanner_pair(ref_scanner, cur_scanner)
                to_be_matched.append(cur_scanner_id)
                matched.add(cur_scanner_id)

    def align_scanner_pair(self, ref_scanner, cur_scanner):
        beacons = [beacon for beacon in cur_scanner.beacons if ref_scanner.id in beacon.matches]
        from_matrix = [beacon.position for beacon in beacons]
        to_matrix = [beacon.matches[ref_scanner.id].real_position for beacon in beacons]
        transformation = find_Nd_to_Nd_transformation(from_matrix, to_matrix)
        for beacon in cur_scanner.beacons:
            beacon.real_position = apply_transformation(beacon.position, transformation).round()
        cur_scanner.position = apply_transformation(Point3D(0, 0, 0), transformation).round()

    def count_all_beacons(self):
        return len({b.real_position for s in self.scanners for b in s.beacons})

    def max_distance_between_scanners(self):
        return max(i.position.manhattan_dist(j.position) for i, j in combinations(self.scanners, 2))


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = BeaconScanner("test1.txt")
    assert test1.count_all_beacons() == 79
    assert test1.max_distance_between_scanners() == 3621

    print("Tests passed, starting with the puzzle")

    beacon_scanner = BeaconScanner(data.input_file)
    print(beacon_scanner.count_all_beacons())
    print(beacon_scanner.max_distance_between_scanners())

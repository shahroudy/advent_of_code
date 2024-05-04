import re
from pathlib import Path

from myutils.io_handler import get_input_data


class ReindeerOlympics:
    def __init__(self, filename):
        self.reindeers = [
            list(map(int, re.findall(r"\d+", line)))
            for line in Path(filename).read_text().splitlines()
        ]

    def calc_distance(self, reindeer, time):
        speed, fly_time, rest_time = reindeer
        cycles = time // (fly_time + rest_time)
        rem_time = time % (fly_time + rest_time)
        return speed * (cycles * fly_time + (fly_time if rem_time >= fly_time else rem_time))

    def max_distance_of_reindeers_after(self, seconds=1000):
        return max(self.calc_distance(reindeer, seconds) for reindeer in self.reindeers)

    def max_score_reindeer_for_all_seconds(self, seconds=1000):
        scores = [0] * len(self.reindeers)
        for second in range(1, seconds + 1):
            winners, max_distance = [], 0
            for index, reindeer in enumerate(self.reindeers):
                distance = self.calc_distance(reindeer, second)
                if distance > max_distance:
                    winners, max_distance = [index], distance
                elif distance == max_distance:
                    winners.append(index)
            for winner in winners:
                scores[winner] += 1
        return max(scores)


if __name__ == "__main__":
    data = get_input_data(__file__)

    test = ReindeerOlympics("sample1.txt")
    assert test.max_distance_of_reindeers_after() == 1120
    assert test.max_score_reindeer_for_all_seconds() == 689

    print("Tests passed, starting with the puzzle")

    puzzle = ReindeerOlympics(data.input_file)

    print(puzzle.max_distance_of_reindeers_after(2503))
    print(puzzle.max_score_reindeer_for_all_seconds(2503))

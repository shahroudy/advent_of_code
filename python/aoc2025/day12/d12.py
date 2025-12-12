from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import read_ints, read_map_dict_of_sets_of_points


class ChristmasTreeFarm:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()
        sections = self.input_text.split("\n\n")

        self.presents = {}
        for s in sections[:-1]:
            lines = s.splitlines()
            index = int(lines[0][:-1])
            points, _, _ = read_map_dict_of_sets_of_points("\n".join(lines[1:]))
            self.presents[index] = points["#"]

        self.regions = []
        for line in sections[-1].splitlines():
            nums = read_ints(text=line)
            self.regions.append([nums[:2], nums[2:]])

    def fitable_regions(self):
        fitable_count = 0
        for region in self.regions:
            (width, height), counts = region
            if width * height >= sum(len(self.presents[i]) * counts[i] for i in range(len(counts))):
                fitable_count += 1
        return fitable_count


if __name__ == "__main__":
    data = get_input_data(__file__)

    puzzle = ChristmasTreeFarm(data.input_file)

    print(puzzle.fitable_regions())

from pathlib import Path

from myutils.io_handler import get_input_data


class SonarSweep:
    def __init__(self, filename):
        self.depths = list(map(int, Path(filename).read_text().splitlines()))

    def depth_increments(self):
        return sum([self.depths[i + 1] > self.depths[i] for i in range(len(self.depths) - 1)])

    def depth_windows_increments(self):
        return sum(self.depths[i + 3] > self.depths[i] for i in range(len(self.depths) - 3))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert SonarSweep("sample1.txt").depth_increments() == 7
    assert SonarSweep("sample1.txt").depth_windows_increments() == 5

    sonar_sweep = SonarSweep(data.input_file)
    print(sonar_sweep.depth_increments())
    print(sonar_sweep.depth_windows_increments())

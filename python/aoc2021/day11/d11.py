from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import read_map_of_digits


class DumboOctopus:
    def __init__(self, filename):
        self.input_text = Path(filename).read_text()
        self.energy_levels, _, _ = read_map_of_digits(self.input_text)

    def _run_step(self, energy_levels):
        new_energy_levels = {octopus: energy + 1 for octopus, energy in energy_levels.items()}
        all_flashed = set()
        while True:
            flashed = {k for k, v in new_energy_levels.items() if v > 9 and k not in all_flashed}
            if not flashed:
                break
            all_flashed.update(flashed)
            for f in flashed:
                for n in f.n8():
                    if n in new_energy_levels and n not in all_flashed:
                        new_energy_levels[n] += 1
        for f in all_flashed:
            new_energy_levels[f] = 0
        return new_energy_levels, len(all_flashed)

    def flash_count(self, step_count=100):
        energy_levels = self.energy_levels.copy()
        flashes = 0
        for _ in range(step_count):
            energy_levels, step_flashes = self._run_step(energy_levels)
            flashes += step_flashes
        return flashes

    def first_step_of_all_flash(self):
        energy_levels = self.energy_levels.copy()
        for step in count(1):
            energy_levels, step_flashes = self._run_step(energy_levels)
            if step_flashes == len(energy_levels):
                return step


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert DumboOctopus("sample1.txt").flash_count(step_count=2) == 9
    assert DumboOctopus("sample2.txt").flash_count() == 1656
    assert DumboOctopus("sample2.txt").first_step_of_all_flash() == 195

    print("Tests passed, starting with the puzzle")

    puzzle = DumboOctopus(data.input_file)

    print(puzzle.flash_count())
    print(puzzle.first_step_of_all_flash())

from pathlib import Path

from myutils.io_handler import get_input_data
from myutils.utils import process_int_list
from myutils.voxel3d import Voxel3D, range3d_intersection, range3d_overlap


class ReactorReboot:
    def __init__(self, filename):
        input_text = Path(filename).read_text()
        values = process_int_list(text=input_text)
        switches = [line[1] == "n" for line in input_text.splitlines()]
        self.steps = [
            (range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1), s)
            for (x1, x2, y1, y2, z1, z2), s in zip(values, switches)
        ]

    def on_cube_count(self, is_init=False):
        if is_init:
            steps = []
            vr = tuple([range(-50, 51) for _ in range(3)])
            for xr, yr, zr, switch in self.steps:
                if intersection := range3d_intersection(vr, (xr, yr, zr)):
                    vrx, vry, vrz = intersection
                    steps.append((vrx, vry, vrz, switch))
        else:
            steps = self.steps

        total = 0
        for i, step in enumerate(steps):
            ranges, switch = step[:3], step[3]
            if not switch:
                continue
            future_overlapping_steps = [r for r in steps[i + 1 :] if range3d_overlap(ranges, r[:3])]
            total += Voxel3D([step] + [r[:3] + (False,) for r in future_overlapping_steps]).volume()
        return total


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = ReactorReboot("test1.txt")
    assert test1.on_cube_count(is_init=True) == 39
    test2 = ReactorReboot("test2.txt")
    assert test2.on_cube_count(is_init=True) == 590784
    test3 = ReactorReboot("test3.txt")
    assert test3.on_cube_count(is_init=True) == 474140
    assert test3.on_cube_count() == 2758514936282235

    print("Tests passed, starting with the puzzle")

    puzzle = ReactorReboot(data.input_file)

    print(puzzle.on_cube_count(is_init=True))
    print(puzzle.on_cube_count())

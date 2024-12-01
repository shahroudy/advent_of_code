import os
from time import time
from pathlib import Path
from myutils.io_handler import get_input_data


class ReactorReboot:
    def __init__(self, filename):
        self.lines = Path(filename).read_text().strip().split("\n")
        self.process()

    def process(self):
        self.steps = []
        for line in self.lines:
            parts = line.split()
            r = [parts[0] == "on"]
            bounds_3D = parts[1].split(",")
            for bounds in bounds_3D:
                limits = bounds[2:].split("..")
                r.append(int(limits[0]))  # inclusive stard
                r.append(1 + int(limits[1]))  # exclusive end
            self.steps.append(r)

    def reboot(self, is_init=False, verbose=False):
        cuts = [set(), set(), set()]
        for step in self.steps:
            for dim in range(3):
                cuts[dim].update(step[1 + dim * 2 : 3 + dim * 2])

        if is_init:
            init_range = [-50, 51]
            for dim in range(3):
                cuts[dim] = {x for x in cuts[dim] if x in range(*init_range)}
                cuts[dim].update(init_range)

        for dim in range(3):
            cuts[dim] = list(cuts[dim])
            cuts[dim].sort()

        sum = 0
        tsum = 0
        for x_cut_idx in range(len(cuts[0]) - 1):
            start_time = time()

            x_sample = cuts[0][x_cut_idx]
            x_range = cuts[0][x_cut_idx + 1] - cuts[0][x_cut_idx]
            x_filtered_steps = []
            for step in self.steps:
                if x_sample in range(step[1], step[2]):
                    x_filtered_steps.append(step)
            for y_cut_idx in range(len(cuts[1]) - 1):
                y_sample = cuts[1][y_cut_idx]
                y_range = cuts[1][y_cut_idx + 1] - cuts[1][y_cut_idx]
                area = x_range * y_range
                y_filtered_steps = []
                for step in x_filtered_steps:
                    if y_sample in range(step[3], step[4]):
                        y_filtered_steps.append(step)
                for z_cut_idx in range(len(cuts[2]) - 1):
                    z_sample = cuts[2][z_cut_idx]
                    for step in reversed(y_filtered_steps):
                        if z_sample in range(step[5], step[6]):
                            switch = step[0]
                            break
                    else:
                        switch = False
                    if switch:
                        z_range = cuts[2][z_cut_idx + 1] - cuts[2][z_cut_idx]
                        sum += area * z_range
            tsum += time() - start_time
            looptime = tsum / (x_cut_idx + 1)
            remaining_time = looptime * (len(cuts[0]) - 2 - x_cut_idx)
            if verbose:
                print(
                    f"Processing {x_cut_idx+1}/{len(cuts[0])-1} "
                    f"Estimated remaining {remaining_time/60:.1f} mins ... "
                    f"Looptime: {looptime:.3f} sec",
                    end="\r",
                )
        if verbose:
            print()
        return sum


if __name__ == "__main__":
    data = get_input_data(__file__)

    test1 = ReactorReboot("test1.txt")
    assert test1.reboot(is_init=True) == 39
    assert test1.reboot(is_init=False) == 39

    test2 = ReactorReboot("test2.txt")
    assert test2.reboot(is_init=True) == 590784

    test3 = ReactorReboot("test3.txt")
    assert test3.reboot(is_init=True) == 474140
    assert test3.reboot(is_init=False) == 2758514936282235

    reactor_reboot = ReactorReboot(data.input_file)
    print(reactor_reboot.reboot(is_init=True))
    print(reactor_reboot.reboot(is_init=False, verbose=True))

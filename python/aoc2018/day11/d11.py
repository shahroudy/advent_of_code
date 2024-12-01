from collections import defaultdict
from pathlib import Path

from myutils.io_handler import get_input_data


class ChronalCharge:
    def __init__(self, serial_no):
        self.serial_no = serial_no
        self.process()

    def process(self):

        self.intgrid = defaultdict(int)

        for x in range(1, 301):
            for y in range(1, 301):
                rack_id = x + 10
                power_level = (rack_id * y + self.serial_no) * rack_id
                power_level = (power_level // 100) % 10 - 5

                self.intgrid[(x, y)] = (
                    power_level
                    + self.intgrid[(x - 1, y)]
                    + self.intgrid[(x, y - 1)]
                    - self.intgrid[(x - 1, y - 1)]
                )

    def calc1(self):
        m = float("-inf")
        for x in range(1, 301 - 2):
            for y in range(1, 301 - 2):
                s = (
                    self.intgrid[(x + 2, y + 2)]
                    + self.intgrid[(x - 1, y - 1)]
                    - self.intgrid[(x + 2, y - 1)]
                    - self.intgrid[(x - 1, y + 2)]
                )
                if s > m:
                    m = s
                    best = x, y

        return ",".join(str(b) for b in best)

    def calc2(self):
        m = float("-inf")
        for x in range(1, 300):
            for y in range(1, 300):
                for ws in range(1, 1 + 300 - max([x, y])):
                    s = (
                        self.intgrid[(x + ws - 1, y + ws - 1)]
                        + self.intgrid[(x - 1, y - 1)]
                        - self.intgrid[(x + ws - 1, y - 1)]
                        - self.intgrid[(x - 1, y + ws - 1)]
                    )
                    if s > m:
                        m = s
                        best = x, y, ws

        return ",".join(str(b) for b in best)


if __name__ == "__main__":
    data = get_input_data(__file__)
    test1 = ChronalCharge(18)
    assert test1.calc1() == "33,45"
    assert test1.calc2() == "90,269,16"

    test2 = ChronalCharge(42)
    assert test2.calc1() == "21,61"
    assert test2.calc2() == "232,251,12"

    chronal_charge = ChronalCharge(int(Path(data.input_file).read_text().strip()))
    print(chronal_charge.calc1())
    print(chronal_charge.calc2())

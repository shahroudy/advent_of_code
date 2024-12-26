import re
from functools import cache, reduce
from itertools import count
from pathlib import Path

from myutils.io_handler import get_input_data


class CrossedWires:
    def __init__(self, filename):
        inputs, gates = Path(filename).read_text().split("\n\n")
        input_re = re.compile(r"(\w+): (\d)")
        self.inputs = {name: int(value) for name, value in input_re.findall(inputs)}
        gates_re = re.compile(r"(\w+) (\w+) (\w+) -> (\w+)")
        self.gates = {out: (op, {left, right}) for left, op, right, out in gates_re.findall(gates)}
        self.all_gates = set(self.gates.keys()) | set(self.inputs.keys())

    @cache
    def get_value(self, name):
        if name in self.inputs:
            return self.inputs[name]
        elif name in self.gates:
            op, (left, right) = self.gates[name]
            if op == "AND":
                return self.get_value(left) & self.get_value(right)
            elif op == "OR":
                return self.get_value(left) | self.get_value(right)
            elif op == "XOR":
                return self.get_value(left) ^ self.get_value(right)
        return None

    def generated_output(self):
        out_gates = sorted([g for g in self.all_gates if g.startswith("z")], reverse=True)
        z_values = [self.get_value(g) for g in out_gates]
        return reduce(lambda x, y: x * 2 + y, z_values)

    def swapped_wires(self):
        swaps = dict()

        def find_gate_name(op, xoy):
            x, y = xoy
            if x in swaps:
                x = swaps[x]
            if y in swaps:
                y = swaps[y]
            for gatei, (opi, xyi) in self.gates.items():
                if (op == opi) and (x in xyi or y in xyi):
                    if x not in xyi:
                        xx = (xyi - {y}).pop()
                        swaps[x] = xx
                        swaps[xx] = x
                    if y not in xyi:
                        yy = (xyi - {x}).pop()
                        swaps[y] = yy
                        swaps[yy] = y
                    return gatei

        carry_in = None
        for bit_counter in count():
            z = f"z{bit_counter:02}"
            x = f"x{bit_counter:02}"
            y = f"y{bit_counter:02}"

            if x not in self.all_gates:
                break

            s = find_gate_name("XOR", {x, y})
            c1 = find_gate_name("AND", {x, y})

            if carry_in is not None:
                zout = find_gate_name("XOR", {s, carry_in})
                c2 = find_gate_name("AND", {s, carry_in})
                carry_in = find_gate_name("OR", {c1, c2})
            else:
                zout = s
                carry_in = c1

            if zout != z:
                swaps[zout] = z
                swaps[z] = zout
        return ",".join(sorted(swaps.keys()))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CrossedWires("sample1.txt").generated_output() == 4
    assert CrossedWires("sample2.txt").generated_output() == 2024

    print("Tests passed, starting with the puzzle")

    puzzle = CrossedWires(data.input_file)

    print(puzzle.generated_output())
    print(puzzle.swapped_wires())

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

    def find_gate_name(self, op, operands, swaps):
        operands = {swaps.get(o, o) for o in operands}
        for out_i, (op_i, operands_i) in self.gates.items():
            if (op == op_i) and (operands & operands_i):
                if operands != operands_i:
                    a = (operands_i - operands).pop()
                    b = (operands - operands_i).pop()
                    swaps[a] = b
                    swaps[b] = a
                return out_i

    def swapped_wires(self):
        swaps = {}
        carry_bit = None
        for bit_counter in count():
            x, y, z = f"x{bit_counter:02}", f"y{bit_counter:02}", f"z{bit_counter:02}"
            if x not in self.all_gates:
                break
            s1 = self.find_gate_name("XOR", {x, y}, swaps)
            c1 = self.find_gate_name("AND", {x, y}, swaps)
            if carry_bit is not None:
                s2 = self.find_gate_name("XOR", {s1, carry_bit}, swaps)
                c2 = self.find_gate_name("AND", {s1, carry_bit}, swaps)
                carry_bit = self.find_gate_name("OR", {c1, c2}, swaps)
            else:
                s2 = s1
                carry_bit = c1
            if s2 != z:
                swaps[s2] = z
                swaps[z] = s2
        return ",".join(sorted(swaps.keys()))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert CrossedWires("sample1.txt").generated_output() == 4
    assert CrossedWires("sample2.txt").generated_output() == 2024

    print("Tests passed, starting with the puzzle")

    puzzle = CrossedWires(data.input_file)

    print(puzzle.generated_output())
    print(puzzle.swapped_wires())

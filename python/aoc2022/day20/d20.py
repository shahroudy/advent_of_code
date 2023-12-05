import os
from pathlib import Path


class GrovePositioningSystem:
    def __init__(self, filename):
        self.numbers = [int(line) for line in Path(filename).read_text().strip().split("\n")]

    def decrypt(self, simple_decryption=True):
        distinct_input = []
        seen_numbers = set()
        for i in self.numbers:
            num = i * (1 if simple_decryption else 811589153)
            while num in seen_numbers:
                if num < 0:
                    num -= 0.001
                else:
                    num += 0.001
            seen_numbers.add(num)
            distinct_input.append(num)

        num_in_pos = {i: v for i, v in enumerate(distinct_input)}
        position = {v: k for k, v in num_in_pos.items()}
        code_len = len(distinct_input)

        for _ in range(1 if simple_decryption else 10):
            for i in distinct_input:
                old_pos = position[i]

                for j in range(old_pos, code_len - 1):
                    num_in_pos[j] = num_in_pos[j + 1]
                    position[num_in_pos[j]] -= 1

                new_pos = 1 + (old_pos - 1 + int(i)) % (code_len - 1)
                for j in range(code_len - 1, new_pos, -1):
                    num_in_pos[j] = num_in_pos[j - 1]
                    position[num_in_pos[j]] += 1
                num_in_pos[new_pos] = i
                position[i] = new_pos

                assert max(position.values()) == code_len - 1
                assert min(position.values()) == 0
                for j in range(code_len):
                    assert position[num_in_pos[j]] == j
        return sum([int(num_in_pos[(position[0] + j * 1000) % code_len]) for j in range(1, 4)])


def test_samples(filename, answer1, answer2):
    test = GrovePositioningSystem(filename)
    assert test.decrypt(simple_decryption=True) == answer1
    assert test.decrypt(simple_decryption=False) == answer2


if __name__ == "__main__":

    test_samples("sample1.txt", 3, 1623178306)

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2022_day20.txt'
    grove_positioning_system = GrovePositioningSystem(input_file)
    print(grove_positioning_system.decrypt())
    print(grove_positioning_system.decrypt(simple_decryption=False))

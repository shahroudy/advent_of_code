from collections import defaultdict, deque
from pathlib import Path

from myutils.io_handler import get_input_data


class MonkeyMarket:
    def __init__(self, filename):
        sells = defaultdict(int)
        self.sum_of_final_secrets = 0
        for initial_secret in [int(n) for n in Path(filename).read_text().splitlines()]:
            secret = initial_secret
            changes = deque()
            seen_change_patterns = set()
            pre_price = secret % 10
            for _ in range(2000):
                secret = (secret * 64 ^ secret) % 16777216
                secret = (secret // 32 ^ secret) % 16777216
                secret = (secret * 2048 ^ secret) % 16777216
                price = secret % 10
                change = price - pre_price
                pre_price = price
                changes.append(change)
                if len(changes) == 4:
                    sequence = tuple(changes)
                    if sequence not in seen_change_patterns:
                        seen_change_patterns.add(sequence)
                        sells[sequence] += price
                    changes.popleft()
            self.sum_of_final_secrets += secret
        self.most_bananas = max(sells.values())


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert MonkeyMarket("sample1.txt").sum_of_final_secrets == 37327623
    assert MonkeyMarket("sample2.txt").most_bananas == 23

    print("Tests passed, starting with the puzzle")

    puzzle = MonkeyMarket(data.input_file)

    print(puzzle.sum_of_final_secrets)
    print(puzzle.most_bananas)

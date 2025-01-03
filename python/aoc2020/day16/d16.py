import re
from collections import defaultdict
from itertools import product
from pathlib import Path

from myutils.exrange import ExRange
from myutils.io_handler import get_input_data
from myutils.utils import multiply


class TicketTranslation:
    def __init__(self, filename):
        rules_txt, ticket_txt, nearby_txt = Path(filename).read_text().split("\n\n")
        rules = {
            re.match(r"^([\w\s]+):", rule).group(): ExRange(
                [range(int(a), int(b) + 1) for a, b in re.findall(r"(\d+)-(\d+)", rule)]
            )
            for rule in rules_txt.splitlines()
        }
        ticket = [int(n) for n in re.findall(r"\d+", ticket_txt)]
        others = [list(map(int, re.findall(r"\d+", t))) for t in nearby_txt.splitlines()[1:]]

        all_ranges = ExRange(list(rules.values()))
        self.ticket_scanning_error_rate = 0
        valid_tickets = []
        for other in others:
            valid = True
            for number in other:
                if number not in all_ranges:
                    self.ticket_scanning_error_rate += number
                    valid = False
            if valid:
                valid_tickets.append(other)

        match = {}
        remaining_names = set(rules.keys())
        remaining_columns = set(range(len(rules)))
        column_values = [[n[col] for n in valid_tickets] for col in remaining_columns]
        possible_matches = defaultdict(set)
        for name, col in product(rules.keys(), remaining_columns):
            if all(value in rules[name] for value in column_values[col]):
                possible_matches[name].add(col)
        while remaining_names:
            for name in remaining_names:
                if len(possible_matches[name] & remaining_columns) == 1:
                    break
            match[name] = (possible_matches[name] & remaining_columns).pop()
            remaining_names.remove(name)
            remaining_columns.remove(match[name])

        self.departure = multiply(ticket[m] for n, m in match.items() if n.startswith("departure"))


if __name__ == "__main__":
    data = get_input_data(__file__)

    assert TicketTranslation("sample1.txt").ticket_scanning_error_rate == 71

    print("Tests passed, starting with the puzzle")

    puzzle = TicketTranslation(data.input_file)

    print(puzzle.ticket_scanning_error_rate)
    print(puzzle.departure)

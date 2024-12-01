import os
from myutils.file_reader import read_line_groups
from myutils.matching import find_a_mapping


class TicketTranslator:

    def __init__(self, filename):
        self.process_input(filename)

    def process_input(self, filename):
        raw_rules, raw_my_ticket, raw_nearby_tickets = read_line_groups(filename)

        # parse the rules
        self.rules = []
        self.rule_names = []
        for line in raw_rules:
            parts = line.split(":")
            rs = parts[1].split("or")
            cr = []
            for r in rs:
                rg = [int(x) for x in r.strip().split("-")]
                cr.append(rg)
            self.rules.append(cr)
            self.rule_names.append(parts[0])

        # parse my ticket
        self.my_ticket = [int(n) for n in raw_my_ticket[1].split(",")]

        # parse nearby tickets
        self.nearby_tickets = []
        for line in raw_nearby_tickets[1:]:
            self.nearby_tickets.append([int(n) for n in line.split(",")])
        return

    def is_valid(self, rule, values):
        for sub_rule_range in rule:
            if sub_rule_range[0] <= values <= sub_rule_range[1]:
                return True
        return False

    def ticket_scanning_error_rate(self):
        error_rate = 0
        self.valid_nearby_tickets = []
        for nearby_ticket in self.nearby_tickets:
            nearby_valid = True
            for value in nearby_ticket:
                valid = False
                for rule in self.rules:
                    if self.is_valid(rule, value):
                        valid = True
                        break
                if not valid:
                    error_rate += value
                    nearby_valid = False
            if nearby_valid:
                self.valid_nearby_tickets.append(nearby_ticket)
        return error_rate

    def match_rules(self):
        # find all the matching columns for each rule
        matched_columns_per_rule = []
        for rule_index in range(len(self.rules)):
            matched_columns = []
            for column_index in range(len(self.valid_nearby_tickets[0])):
                for nearby_ticket in self.valid_nearby_tickets:
                    if not self.is_valid(self.rules[rule_index], nearby_ticket[column_index]):
                        break
                else:
                    matched_columns.append(column_index)
            matched_columns_per_rule.append([rule_index, matched_columns])

        mapped_column = find_a_mapping(matched_columns_per_rule)

        # find the multiplication of 'departure' related colums in my ticket
        result = 1
        for rule in range(len(self.rules)):
            if "departure" in self.rule_names[rule]:
                result *= self.my_ticket[mapped_column[rule]]
        return result


if __name__ == "__main__":
    test1 = TicketTranslator("test1.txt")
    assert test1.ticket_scanning_error_rate() == 71

    input_file = f'{os.environ.get("aoc_inputs")}/aoc2020_day16.txt'
    ticket_translator = TicketTranslator(input_file)
    print(ticket_translator.ticket_scanning_error_rate())  # 23009
    print(ticket_translator.match_rules())  # 10458887314153

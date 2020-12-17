from typing import List, NamedTuple, Tuple

from math import prod


def parse_input(input_data: str) -> dict:
    data = {}
    d = input_data.strip().split("\n\n")
    data["rules"] = [i.strip() for i in d[0].strip().split("\n")]
    data["my_ticket"] = [int(i) for i in d[1].split("\n")[1].strip().split(",")]
    data["other_tickets"] = [
        [int(i) for i in ticket.strip().split(",")] for ticket in d[2].split("\n")[1:]
    ]
    return data


class Rule(NamedTuple):
    field_name: str
    lo1: int
    hi1: int
    lo2: int
    hi2: int

    def is_valid_value(self, value: int) -> bool:
        if (self.lo1 <= value <= self.hi1) or (self.lo2 <= value <= self.hi2):
            return True
        else:
            return False

    @staticmethod
    def parse_line(line: str) -> Tuple:
        field_name, parts = line.strip().split(": ")
        low_range, hi_range = parts.split(" or ")
        lo1, hi1 = [int(i) for i in low_range.split("-")]
        lo2, hi2 = [int(i) for i in hi_range.split("-")]
        return Rule(field_name, lo1, hi1, lo2, hi2)


def is_valid_ticket(rules: List[Rule], ticket) -> bool:
    for value in ticket:
        if not any([rule.is_valid_value(value) for rule in rules]):
            return False
    return True


def solve1(input_data: str) -> int:
    data = parse_input(input_data)
    rules = [Rule.parse_line(line) for line in data["rules"]]
    ticket_values = [
        value for ticket in data["other_tickets"] for value in ticket
    ]  # flatten lists of values in list of tickets

    invalids = []

    for value in ticket_values:
        rules_check = [rule.is_valid_value(value) for rule in rules]
        if not any(rules_check):
            invalids.append(value)

    return sum(invalids)


def find_fields(input_data):
    """Return {'field_name': index} indicating the position of the fields in the tickets"""
    data = parse_input(input_data)
    rules = [Rule.parse_line(line) for line in data["rules"]]
    valid_tickets = [
        ticket for ticket in data["other_tickets"] if is_valid_ticket(rules, ticket)
    ]

    ticket_list = []

    # replace every value in each ticket with the set of rules that it passes
    for ticket in valid_tickets:
        value_list = []
        for value in ticket:
            passing_rules = set()
            for rule in rules:
                if rule.is_valid_value(value):
                    passing_rules.add(rule.field_name)
            value_list.append(passing_rules)
        ticket_list.append(value_list)

    # transpose. Ticket list[0] will represent the first item on each ticket rather than the first ticket
    ticket_list = [
        [row[i] for row in ticket_list] for i, _ in enumerate(ticket_list[0])
    ]
    rule_possibilities = [set.intersection(*item) for item in ticket_list]

    selected = {}
    while any(map(lambda x: len(x) > 0, rule_possibilities)):
        for i, value in enumerate(rule_possibilities):
            if len(value) == 1:
                selected[next(iter(value))] = i
                for i, item in enumerate(rule_possibilities):
                    rule_possibilities[i] = item.difference(value)

    return selected


def solve2(input_data: str) -> int:
    data = parse_input(input_data)
    fields = find_fields(input_data)
    idxs = [
        fields[field] for field in fields.keys() if field.split(" ")[0] == "departure"
    ]

    return prod(data["my_ticket"][i] for i in idxs)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """class: 1-3 or 5-7
    row: 6-11 or 33-44
    seat: 13-40 or 45-50

    your ticket:
    7,1,14

    nearby tickets:
    7,3,47
    40,4,50
    55,2,20
    38,6,12"""

    additional_test_data = """class: 0-1 or 4-19
                            row: 0-5 or 8-19
                            seat: 0-13 or 16-19

                            your ticket:
                            11,12,13

                            nearby tickets:
                            3,9,18
                            15,1,5
                            5,14,9
                            """

    assert solve1(test_data) == 71

    puz16 = Puzzle(2020, 16)
    input_data = puz16.input_data
    puz16.answer_a = solve1(input_data)
    puz16.answer_b = solve2(input_data)

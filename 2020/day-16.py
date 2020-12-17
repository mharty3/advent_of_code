from typing import NamedTuple, Tuple


def parse_input(input_data):
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


def solve1(input_data):
    data = parse_input(input_data)
    rules = [Rule.parse_line(line) for line in data["rules"]]
    ticket_values = [
        i for ticket in data["other_tickets"] for i in ticket
    ]  # flatten list

    invalids = []

    for value in ticket_values:
        rules_check = [rule.is_valid_value(value) for rule in rules]
        if not any(rules_check):
            invalids.append(value)

    return sum(invalids)


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

    assert solve1(test_data) == 71

    puz16 = Puzzle(2020, 16)
    input_data = puz16.input_data
    puz16.answer_a = solve1(input_data)
    # puz16.answer_b = solve2(input_data)

from __future__ import annotations
import re
from typing import NamedTuple



class Rule(NamedTuple):
    number: str
    terms: str

    @staticmethod
    def parse_from_line(line: str) -> Rule:
        number, parts = line.strip().split(": ")
        return Rule(number, parts.replace('"', ''))
        
    def expand_rule(self, rules):
        s = self.terms
        while re.search('\d+ ', s):
            for i in re.findall('\d', s):
                s = s.replace(i, f'({rules[i].terms})')
        print(self._replace(terms=s.replace(' ', '')))
        return self._replace(terms=s.replace(' ', ''))


class Problem(NamedTuple):
    rules: dict
    messages : list

    @staticmethod
    def parse_problem(input_data):
        rules_section, messages = input_data.strip().split('\n\n')
        rules = [Rule.parse_from_line(line) for line in rules_section.split('\n')]
        rules = {rule.number: rule for rule in rules}

        messages = [m.strip() for m in messages.split('\n')]

        return Problem(rules, messages)


def solve1(input):
    prob = Problem.parse_problem(input)
    prob.rules['0'] = prob.rules['0'].expand_rule(prob.rules)
    return sum([bool(re.fullmatch(prob.rules['0'].terms, message)) for message in prob.messages])


if __name__ == "__main__":

    from aocd.models import Puzzle

    test_input = """0: 4 1 5
                    1: 2 3 | 3 2
                    2: 4 4 | 5 5
                    3: 4 5 | 5 4
                    4: "a"
                    5: "b"

                    ababbb
                    bababa
                    abbbab
                    aaabbb
                    aaaabbb"""

    assert solve1(test_input) == 2

    puz19 = Puzzle(2020, 19)
    data = puz19.input_data
    # puz19.answer_a = solve1(data)
    # puz19.answer_b = solve2(data)
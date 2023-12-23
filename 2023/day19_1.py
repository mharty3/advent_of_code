from dataclasses import dataclass
from typing import Optional
from aocd.models import Puzzle

puzzle = Puzzle(2023, 19)
input_data = puzzle.input_data


@dataclass
class Rule:
    destination: str
    attribute: Optional[str] = None
    operator: Optional[str] = None
    comp_value: Optional[int] = None

    @staticmethod
    def parse(input_str):
        if ':' in input_str:
            check, dest = input_str.split(':')
            attribute = check[0]
            operator = check[1]
            comp_value = int(check[2:])
            return Rule(dest, attribute, operator, comp_value)
        
        else:
            return Rule(destination=input_str)
        
    def _compare(self, value):
        if self.operator == '>':
            return value > self.comp_value
        else:
            return value < self.comp_value
        
    def evaluate(self, part):
        if not self.attribute:
            return self.destination
        else:
            if self._compare(part[self.attribute]):
                return self.destination


@dataclass
class Workflow:
    rules: list[Rule]

    @staticmethod
    def parse(input_str):
        rules = []
        for raw_rule in input_str.split(','):
            rules.append(Rule.parse(raw_rule))
        return Workflow(rules)
    
    def evaluate(self, part):
        for rule in self.rules:
            if dest := rule.evaluate(part):
                part['workflow'] = dest
                return part
    

def parse(input_data):
    workflow_raw, parts_raw = input_data.split('\n\n')

    workflows = dict()
    for w in workflow_raw.split():
        name, rules_str = w.replace('}', '').split('{')
        workflows[name] = Workflow.parse(rules_str)

    parts = list()
    for p in parts_raw.split():
        part = dict(workflow='in')
        for a in p.replace('{', '').replace('}', '').split(','):
            attr, val = a.split('=')
            part[attr] = int(val)
        parts.append(part)

        
    return workflows, parts


def solve1(input_data):
    workflows, parts = parse(input_data)

    accepted_parts = []
    for p in parts:

        while p['workflow'] not in ['A', 'R']:
            p = workflows[p['workflow']].evaluate(p)
            if p['workflow'] == 'A':
                accepted_parts.append(p)

    return sum([p['x'] + p['m'] + p['a'] + p['s'] for p in accepted_parts])



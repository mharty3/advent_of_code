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



class Node:

    def __init__(self, value = None):
        self.left  = None
        self.right = None
        self.value = value


class DecisionNode:

    def __init__(self, left=None, right=None, left_name=None, right_name=None,
                 attribute=None, threshold=None, 
                 x_range=(0, 4000), m_range=(0, 4000), a_range=(0, 4000), s_range=(0, 4000)):
        
        self.left  = left
        self.right = right

        self.left_name = left_name
        self.right_name = right_name

        self.name = None

        self.attribute = attribute
        self.threshold = threshold

        self.x_range = x_range
        self.m_range = m_range
        self.a_range = a_range
        self.s_range = s_range

    def __repr__(self):
        return f"{{{self.attribute}<{self.threshold}:{self.left},{self.right}}}"
    
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # Then print the data of node
        print(root, end=" "),

        # Now recur on right child
        printInorder(root.right)
        

nodes = {}

nodes['in'] = DecisionNode(attribute='s', threshold=1351, left_name='px', right_name='qqz')
nodes['px'] = DecisionNode(attribute='a', threshold=2006, left_name='qkq', right=DecisionNode(attribute='m', threshold=2090, right_name='A', left_name='rfg'))

test_data = """

in{s<1351:px,qqz}
px{a<2006:qkq,m>2090:A,rfg}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
hdj{m>838:A,pv}

rfg{s<537:gd,x>2440:R,A}
lnx{m>1548:A,A}
pv{a>1716:R,A}

crn{x>2662:A,R}
gd{a>3333:R,R}
qqz{s>2770:qs,m<1801:hdj,R}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

r"""
                                    in{s<1351:px,qqz}
                         /                                  \
px{a<2006:qkq,m>2090:A,rfg}                                        qqz{s>2770:qs,m<1801:hdj,R}
       /            |      \                                        /             |               \
qkq{x<1416:A,crn}   A       rfg{s<537:gd,x>2440:R,A}         qs{s>3448:A,lnx}    hdj{m>838:A,pv}    R
    /    \                         /          |   \             /         \                 /  \
   A     crn{x>2662:A,R}     gd{a>3333:R,R}   R    A           A       lnx{m>1548:A,A}     A  pv{a>1716:R,A}
            /  \                 /   \                                      /  \
           A    R               R     R                                    A    A

        

           
           

            s < 1351        
              /  \
            qqz    a < 2006
                     /    \
                 m < 2090   qkq
                   /  \
                rfg    A 

              """
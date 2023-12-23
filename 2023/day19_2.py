from dataclasses import dataclass
from typing import Optional
from copy import deepcopy
import uuid
import graphviz

from aocd.models import Puzzle
puzzle = Puzzle(2023, 19)
input_data = puzzle.input_data


class DecisionNode:

    def __init__(self, child1=None, child2=None, 
                 c1_name=None, c2_name=None,
                 attribute=None, threshold=None, operator=None,
                 ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
                 ):
        
        if operator == '>':
            self.left  = child2
            self.right = child1
            self.left_name = c2_name
            self.right_name = c1_name
            self.threshold = threshold + 1

        elif operator == '<':
            self.left  = child1
            self.right = child2
            self.left_name = c1_name
            self.right_name = c2_name
            self.threshold = threshold

        else:
            self.left = None
            self.right = None
            self.left_name = None
            self.right_name = None
            self.threshold = None

        self.name = str(uuid.uuid4())

        self.attribute = attribute
        self.ranges = ranges

    def __repr__(self):
        if self.attribute in ['x', 'm', 'a', 's']:
            return f"{{{self.attribute}<{self.threshold}: \n {self.left if self.left else self.left_name}, {self.right if self.right else self.right_name}}}"
        
        return f'{self.attribute}'
    

def build_node(node_list, i=0):
    if i >= len(node_list):
        return None

    node = node_list[i]
    if '>' in node or '<' in node:
        attr = node[0]
        op = node[1]
        threshold = int(node[2:])

        if '<' in node_list[i+1] or '>' in node_list[i+1]:
            c1 = build_node(node_list, i+1)
            c1_name = None
        else:
            c1_name = node_list[i+1]
            c1 = None

        if '<' in node_list[i+2] or '>' in node_list[i+2]:
            c2 = build_node(node_list, i+2)
            c2_name = None
        else:
            c2_name = node_list[i+2]
            c2 = None


        node = DecisionNode(attribute=attr, 
                            operator=op, 
                            threshold=threshold,
                            c1_name=c1_name,
                            c2_name=c2_name,
                            child1=c1,
                            child2=c2
                            )

    return node


def parse2(input_data):
    workflow_raw, _ = input_data.split('\n\n')

    workflows = dict()
    for w in workflow_raw.split():
        name, rules_str = w.replace('}', '').split('{')
        # print(name, rules_str.replace(':', ',').split(','))
        workflows[name] = build_node(rules_str.replace(':', ',').split(','))

    workflows['A'] = DecisionNode(attribute='A')
    workflows['R'] = DecisionNode(attribute='R')
        
    return workflows


def connect_tree(root, nodes):
    if root.attribute == 'A':
        return DecisionNode(attribute='A')
    elif root.attribute == 'R':
        return DecisionNode(attribute='R')    

    if root.left_name:# and root.left_name not in ['A', 'R']:
        root.left = connect_tree(nodes[root.left_name], nodes)
    else:
        root.left = connect_tree(root.left, nodes)

    if root.right_name:# and root.right_name not in ['A', 'R']:
        root.right = connect_tree(nodes[root.right_name], nodes)
    else:
        root.right = connect_tree(root.right, nodes)

    return deepcopy(root)


def analyze_tree(t):
    n = t
    dot = graphviz.Digraph()
    node_list = [n]
    accepted_ranges = []
    dot.node(name=n.name, label=f'{n.attribute}<{n.threshold}\n{n.ranges}', shape='box')

    while node_list:
        n = deepcopy(node_list.pop())

        if n.left:
            n.left.ranges = deepcopy(n.ranges)
            n.left.ranges[n.attribute] = deepcopy((n.ranges[n.attribute][0], n.threshold-1))

            if n.left.attribute == 'A':
                accepted_ranges.append(n.left.ranges)
                dot.node(name=n.left.name, label=f'{n.left.attribute}', color='green', shape='box')  


            
            dot.node(name=n.left.name, label=f'{n.left.attribute}<{n.left.threshold}\n{n.left.ranges}', shape='box', )  
            dot.edge(n.name, n.left.name)
            
            node_list.append(deepcopy(n.left))
        
        if n.right:
            n.right.ranges = deepcopy(n.ranges)
            n.right.ranges[n.attribute] = deepcopy((n.threshold, n.ranges[n.attribute][1]))

            if n.right.attribute == 'A':
                accepted_ranges.append(n.right.ranges)
                dot.node(name=n.right.name, label=f'{n.right.attribute}', color='green', shape='box')  

            
            dot.node(name=n.right.name, label=f'{n.right.attribute}<{n.right.threshold}\n{n.right.ranges}', shape='box')  
            dot.edge(n.name, n.right.name)
            
            node_list.append(deepcopy(n.right))
    
    return dot, accepted_ranges 


def solve2(input_data):
    nodes = parse2(input_data)
    t = connect_tree(nodes['in'], nodes)
    dot, accepted_ranges = analyze_tree(t)


    total = 0
    for r in accepted_ranges:
        subtotal = 1
        for attr_range in r.values():
            subtotal *= (len(range(*attr_range)) + 1)
        total += subtotal

    return dot, total


dot, total = solve2(input_data)
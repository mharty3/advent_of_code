from collections import deque
from typing import Tuple

from aocd.models import Puzzle
puzzle = Puzzle(2023, 20)
input_data = puzzle.input_data

# pulse = (source, target, pulse_val)

class FlipFlop:
    def __init__(self, name, downstream_modules):
        self.name = name
        self.state = 'off'
        self.downstream_modules = downstream_modules

    def pulse(self, in_pulse):
        source_module, target, pulse_val = in_pulse
        if pulse_val == 'low' and self.state == 'off':
            self.state = 'on'
            out_pulse_val = 'high'
            
            return [(self.name, target, out_pulse_val) for  target in self.downstream_modules]
        
        if pulse_val == 'low' and self.state == 'on':
            self.state = 'off'
            out_pulse_val = 'low'

            return [(self.name, target, out_pulse_val) for  target in self.downstream_modules]
        
    

class ConjunctionModule:
    def __init__(self, name, input_modules, downstream_modules):
        self.name = name
        self.downstream_modules = downstream_modules
        self.input_states = {module: 'low' for module in input_modules}

    def pulse(self, in_pulse):
        source_module, target_module, pulse_val = in_pulse
        self.input_states[source_module] = pulse_val

        if 'low' in self.input_states.values():
            out_pulse_val = 'high'
        else:
            out_pulse_val = 'low'
        
        return [(self.name, target, out_pulse_val) for target in self.downstream_modules]



def parse(input_data):
    module_connections = dict()    
    module_types = dict()
    
    for line in input_data.splitlines():
        m, out = line.split(' -> ')
        m_name = m.replace('%', '').replace('&', '')
        module_connections[m_name] = out.split(', ')

        if m.startswith('%'):
            module_types[m_name] = '%'
        elif m.startswith('&'):
            module_types[m_name] = '&'


    modules = dict()
    for module, type_ in module_types.items():
        if type_ == '%':
            modules[module] = FlipFlop(name=module, 
                                       downstream_modules=module_connections[module])
        elif type_ == '&':
            upstream_modules = [k for k, v in module_connections.items() if module in v]
            modules[module] = ConjunctionModule(name=module,
                                                input_modules=upstream_modules,
                                                downstream_modules=module_connections[module])

    queue = deque()        
    for pulse in [('broadcaster', m, 'low') for m in module_connections['broadcaster']]:
        queue.append(pulse)
    
    return modules, queue


test_1 = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

test_2 = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""

def solve1(input_data):
    modules, initial_queue = parse(input_data)

    low = 0
    high = 0

    for i in range(1000): # push the button 1000x
        low += 1 # the button gives one low pulse
        queue = initial_queue.copy() # reset the queue to the broadcaster's output

        while queue:
            pulse = queue.popleft() # get the next pulse and add the value to the counters
            
            if pulse[2] == 'low':
                low += 1
            
            elif pulse[2] == 'high':
                high += 1
            
            target_module = modules.get(pulse[1], None)
            if target_module:    
                if out_pulse := target_module.pulse(pulse): # generate output pulses and add them to the queue
                    for p in out_pulse:
                        queue.append(p)

    return low * high


def solve2_brute_force(input_data):
    # will probably never finish
    modules, initial_queue = parse(input_data)

    button_presses = 0
    while True:
        
        button_presses += 1
        queue = initial_queue.copy()

        while queue:
            pulse = queue.popleft()
            target_module = modules.get(pulse[1], None)
            if target_module:    
                if out_pulse := target_module.pulse(pulse):
                    for p in out_pulse:
                        queue.append(p)
                        if p[1] == 'rx' and p[2] == 'low':
                            return button_presses


answer_a = solve1(input_data)


    




"""
Rocket Equation
https://adventofcode.com/2019/day/1
"""

def fuel_required(mass):
    return mass // 3 - 2

assert fuel_required(12) == 2
assert fuel_required(14) == 2
assert fuel_required(1969) == 654
assert fuel_required(100756) == 33583 

def fuel_required_including_added_fuel_weight(mass):
    fuel = fuel_required(mass)
    fuel_for_fuel = fuel_required(fuel)
    total_additional_fuel = fuel_for_fuel
    while fuel_for_fuel > 0:
        fuel_for_fuel = fuel_required(fuel_for_fuel)
        if fuel_for_fuel > 0:
            total_additional_fuel += fuel_for_fuel
    return fuel + total_additional_fuel

assert fuel_required_including_added_fuel_weight(14) == 0
assert fuel_required_including_added_fuel_weight(1969) == 966
assert fuel_required_including_added_fuel_weight(100756) == 50346



def parse(input_data):
    return [int(mass) for mass in input_data.strip().split("\n")]

def solve1(input_data):
    modules = parse(input_data)
    return sum([fuel_required(module) for module in modules])

def solve2(input_data):
    modules = parse(input_data)
    return(sum([fuel_required_including_added_fuel_weight(module) for module in modules]))

if __name__ == "__main__":
    from aocd.models import Puzzle
    puzzle = Puzzle(2019, 1)
    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2

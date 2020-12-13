def solve1(input_data):
    lines = input_data.split("\n")
    time_available = int(lines[0])
    buses = lines[1].strip().split(",")
    buses = [int(bus) for bus in buses if bus != "x"]
    time_until_next_bus = [bus - (time_available % bus) for bus in buses]

    minutes_to_wait = min(time_until_next_bus)
    next_bus_id = buses[time_until_next_bus.index(minutes_to_wait)]

    return minutes_to_wait * next_bus_id


if __name__ == "__main__":

    from aocd.models import Puzzle

    test_data = """939
                7,13,x,x,59,x,31,19"""

    assert solve1(test_data) == 295

    puz13 = Puzzle(2020, 13)
    data = puz13.input_data
    puz13.answer_a = solve1(data)
    # puz13.answer_b = solve2(data)

from collections import deque

s = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
    
    """


def parse(input_data):
    barrel = dict()
    raw_monkeys = input_data.split('\n\n')
    for monkey in raw_monkeys:
        lines = monkey.splitlines()

        # number
        number = int(lines[0].split(' ')[-1].replace(':', ''))
        
        # items
        print(lines[1])
        _, items_raw = lines[1].split(':')
        items = deque([int(i) for i in items_raw.split(', ')])
        
        # operation
        _, op_raw = lines[2].split("= ")
        operation = eval(f'lambda old: {op_raw}')
        
        # test
        test_val = int(lines[3].split(' ')[-1])
        test = eval(f'lambda i: i % {test_val} == 0')

        # true dest
        true_dest = int(lines[4].split(' ')[-1])

        # false dest
        false_dest = int(lines[5].split(' ')[-1])
            



        barrel[number] = Monkey(items=items,
                                operation=operation,
                                test=test,
                                true_dest=true_dest,
                                false_dest=false_dest)

    return barrel


class Monkey:
    def __init__(self, items, operation, test, true_dest, false_dest) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest
        self.counter = 0


    def inspect(self):
        item = self.items.popleft()
        item = self.operation(item) // 3
        self.counter += 1

        if self.test(item):
            return self.true_dest, item
        else:
            return self.false_dest, item


    def turn(self):
        while len(self.items) > 0:
            yield self.inspect()


    def catch(self, item):
        self.items.append(item)

barrel = dict()

barrel[0] = Monkey(deque((79, 98)),
                   lambda i: i * 19,
                   lambda i: i % 23 == 0,
                   true_dest=2,
                   false_dest=3)

barrel[1] = Monkey(deque((54, 65, 75, 74)),
                   lambda i: i + 6,
                   lambda i: i % 19 == 0,
                   true_dest=2,
                   false_dest=0)

barrel[2] = Monkey(deque((79, 60, 97)),
                   lambda i: i * i,
                   lambda i: i % 13 == 0,
                   true_dest=1,
                   false_dest=3)

barrel[3] = Monkey(deque([74]),
                   lambda i: i + 3,
                   lambda i: i % 17 == 0,
                   true_dest=0,
                   false_dest=1)


def solve(input_data, n):
    barrel = parse(input_data)
    for round in range(n):
        for monkey in barrel.values():
            for dest, item in monkey.turn():
                barrel[dest].catch(item)
    counts = [m.counter for m in barrel.values()]
    counts.sort()
    return counts[-1] * counts[-2]



if __name__ == '__main__':

    from aocd.models import Puzzle
    puzzle = Puzzle(2022, 11)

    answer_1 = solve(puzzle.input_data, 20)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve(puzzle.input_data, 10_000)
    print(answer_2)
    puzzle.answer_b = answer_2
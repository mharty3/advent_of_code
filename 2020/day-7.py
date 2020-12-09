def parse_dict(input_data):
    """Return a rules dict of the format:
    {
    'light red': [(1, 'bright white'), (2, 'muted yellow')],
    'dark orange': [(3, bright white), (4, muted yellow)],
    'faded blue': [(0, 'bags')]
    }
    """
    
    bags = dict()
    for line in input_data.split('\n'):
        outer, inner = line.strip().split(' bags contain ')
        inner = [i.split(' ') for i in inner.split(", ")]
        if 'no' in inner[0]:
            bags[outer] = [(0, 'bags')]
        else:
            bags[outer] = [(int(i[0]), ' '.join(i[1:3])) for i in inner]
    return bags


def find_carriers(rules, inner_color):
    """Return a list of bag colors that contain the bag of the given inner color"""
    
    valid_bags = []
    for outer, inners in rules.items():
        inners_list = [i[1] for i in inners]
        if inner_color in inners_list:
            valid_bags.append(outer)
    return valid_bags


def solve1(input_data):
    rules_dict = parse_dict(input_data)
    
    carriers = ['shiny gold']
    for carrier in carriers:
        valid_bags = find_carriers(rules_dict, carrier)
        for bag in valid_bags:
            if bag not in carriers:
                # append to the list i'm iterating over. Probably a bad idea. But it works
                carriers.append(bag) 
    return len(carriers) - 1 # subtract 1 to not count the shiny gold bag


def bag_count(rules, count, bag_color, cum_count):  
    if count == 0:
        return 1

    for inner_bag in rules[bag_color]:
        inner_count, inner_color = inner_bag
        cum_count += inner_count * bag_count(rules, inner_count, inner_color, 1)
    return cum_count


def solve2(input_data):
    rules_dict = parse_dict(input_data)
    return bag_count(rules_dict, 1, 'shiny gold', 0)


if __name__ == "__main__":
    from aocd.models import Puzzle

    test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
        dark orange bags contain 3 bright white bags, 4 muted yellow bags.
        bright white bags contain 1 shiny gold bag.
        muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
        shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
        dark olive bags contain 3 faded blue bags, 4 dotted black bags.
        vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
        faded blue bags contain no other bags.
        dotted black bags contain no other bags."""

    additional_test_data = """shiny gold bags contain 2 dark red bags.
        dark red bags contain 2 dark orange bags.
        dark orange bags contain 2 dark yellow bags.
        dark yellow bags contain 2 dark green bags.
        dark green bags contain 2 dark blue bags.
        dark blue bags contain 2 dark violet bags.
        dark violet bags contain no other bags."""

    assert solve1(test_data) == 4
    assert solve2(test_data) == 32
    assert solve2(additional_test_data) == 126

    puz7 = Puzzle(2020, 7)
    data = puz7.input_data
    puz7.answer_a = solve1(data)
    puz7.answer_b = solve2(data)
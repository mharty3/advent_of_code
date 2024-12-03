def parse(input_data):
    reports = [
        [int(level) for level in line.split()] 
        for line in input_data.strip().splitlines()
        ]
    return reports


def is_safe(report):
    is_increasing = report[1] - report[0] > 0
    for level_1, level2 in zip(report, report[1:]):
        diff = level2 - level_1
        
        if abs(diff) == 0 or abs(diff) > 3:
            return False
        
        if (diff > 0) != is_increasing:
            return False
    return True


def solve1(input_data):
    return sum([is_safe(report) for report in parse(input_data)])


def is_safe2(report):
    """Brute Force Solution"""
    if is_safe(report):
        return True
    
    else:
        for i, _ in enumerate(report):
            report_copy = report.copy()
            report_copy.pop(i)
            if is_safe(report_copy):
                return True
        return False

def is_safe3(report):
    """
    faster solution that I tried first, 
    but didn't realize I needed to check the index prior to the failing index
    until I got some edge case examples from a reddit post.
    https://www.reddit.com/r/adventofcode/comments/1h4shdu/2024_day_2_part2_edge_case_finder/
    """
    if is_safe(report):
        return True
    
    is_increasing = report[1] - report[0] > 0
    first_failing_index = None
    for i, (level_1, level2) in enumerate(zip(report, report[1:])):
        diff = level2 - level_1

        if abs(diff) == 0 or abs(diff) > 3:
            first_failing_index = i
            break
        
        if (diff > 0) != is_increasing:
            first_failing_index = i
            break

    report_copy = report.copy()
    report_copy2 = report.copy()
    report.pop(first_failing_index)
    report_copy.pop(first_failing_index + 1)
    report_copy2.pop(first_failing_index - 1)
    return is_safe(report) or is_safe(report_copy) or is_safe(report_copy2)

def solve2(input_data):
    return sum([is_safe2(report) for report in parse(input_data)])
        
        
if __name__ == '__main__':
    from aocd.models import Puzzle

    puzzle = Puzzle(2024, 2)
    input_data = puzzle.input_data

    answer_1 = solve1(puzzle.input_data)
    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(input_data)
    
    print(answer_2)
    puzzle.answer_b = answer_2
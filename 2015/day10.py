def look_and_say(input_str):
    consecutive_d = 1
    output_str = ''
    for i, d in enumerate(input_str):
        if len(input_str) == i+1:
            continue
        elif d == input_str[i+1]:
            consecutive_d += 1
        else:
            output_str += f'{consecutive_d}{d}'
            consecutive_d = 1
    else:
       output_str += f'{consecutive_d}{d}' 
    return output_str

def solve1(input_str):
    for _ in range(40):
        input_str = look_and_say(input_str)
    
    return len(input_str)


def solve2(input_str):
    for _ in range(50):
        input_str = look_and_say(input_str)
    
    return len(input_str)

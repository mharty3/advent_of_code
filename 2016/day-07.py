# --- Day 7: Internet Protocol Version 7 ---

import re

def is_abba(text: str) -> bool:
    return (len(text) == 4 and 
            len(set(text)) == 2 and
            text[:2] == text[::-1][:2])


def is_aba(text: str) -> bool:
    return (len(text) == 3 and 
            len(set(text)) == 2 and
            text[0] == text[-1])


def contains_abba(text:str) -> bool:
    for i, letter in enumerate(text):
        sub_s = text[i:i+4]
        if is_abba(sub_s):
            return True
    return False

def supports_tls(ip_address):
    brackets = re.findall('\[.*?\]', ip_address)
    for bracket in brackets:
        if contains_abba(bracket):
            return False
    return contains_abba(ip_address)
    
    
def supports_ssl(ip_address: str) -> bool:
    brackets = re.findall('\[.*?\]', ip_address)
    non_brackets = ip_address
    for b in brackets:
        non_brackets = non_brackets.replace(b, ',')
    non_brackets = non_brackets.split(',')

    for nb in non_brackets:
        for i, _ in enumerate(nb):
            sub_s = nb[i:i+3]
            if is_aba(sub_s):
                bab = sub_s[1] + sub_s[0] + sub_s[1]      
                for b in brackets:
                    if bab in b:
                        return True
    return False
        
    

    




assert supports_tls('abba[mnop]qrst')       # supports TLS (abba outside square brackets)
assert not supports_tls('abcd[bddb]xyyx')   # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
assert not supports_tls('aaaa[qwer]tyui')   # does not support TLS (aaaa is invalid; the interior characters must be different).
assert supports_tls('ioxxoj[asdfgh]zxcvbn') # supports TLS (oxxo is outside square brackets, even though it's within a larger string).


assert supports_ssl('aba[bab]xyz')         # supports SSL (aba outside square brackets with corresponding bab within square brackets).
assert not supports_ssl('xyx[xyx]xyx')         # does not support SSL (xyx, but no corresponding yxy).
assert supports_ssl('aaa[kek]eke')         # supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
assert supports_ssl('zazbz[bzb]cdb')       # supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).



def solve1(input_data):
    addresses = input_data.split('\n')
    supports = [supports_tls(address) for address in addresses]
    return sum(supports)


def solve2(input_data):
    addresses = input_data.split('\n')
    supports = [supports_ssl(address) for address in addresses]
    return sum(supports)

if __name__ == '__main__':
    from aocd.models import Puzzle
    puzzle = Puzzle(2016, 7)
    answer_1 = solve1(puzzle.input_data)

    print(answer_1)
    puzzle.answer_a = answer_1

    answer_2 = solve2(puzzle.input_data)
    print(answer_2)
    puzzle.answer_b = answer_2
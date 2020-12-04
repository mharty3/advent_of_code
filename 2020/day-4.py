import re

def parse(input_data):
    "Return list of dictionaries representing passports with key value pairs"
    passport_strings = re.split('\n\n', input_data)
    # split on whitespace to create lists of key value pairs for each passport
    field_lists = [re.split('\s', p) for p in passport_strings]
    
    passports = list()
    for field_list in field_lists: # for loop to avoid overly nested comprehensions
        d = {k:v for k, v in [(f.split(':')) for f in field_list]}
        passports.append(d)
    return passports


def validate_passport(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    optional_fields = {'cid'}
    
    keys = set(passport.keys())
    return keys == required_fields or keys == required_fields.union(optional_fields)


def validate_passport_values(passport):
    # byr
    if not (re.match("\d{4}", passport['byr']) and (1920 <= int(passport['byr']) <= 2002)):
        return False
    # iyr
    if not (re.match("\d{4}", passport['iyr']) and (2010 <= int(passport['iyr']) <= 2020)):
        return False
    # eyr
    if not (re.match("\d{4}", passport['eyr']) and (2020 <= int(passport['eyr']) <= 2030)):
        return False
    # hgt
    if not re.match("\d*(cm|in)$", passport['hgt']):
        return False
    if 'cm' in passport['hgt']:
        if not 150 <= int(passport['hgt'][0:-2]) <= 193:
            return False
    if 'in' in passport['hgt']:
        if not 59 <= int(passport['hgt'][0:-2]) <= 76:
            return False
    # hcl
    if not re.match("#[0-9a-f]{6}", passport['hcl']):
        return False
    # ecl
    allowed_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not passport['ecl'] in allowed_ecl:
        return False
    # pid
    if not re.match('\d{9}$', passport['pid']):
        return False
    return True                 


def solve(input_data):
    passports = parse(input_data)
    return len([p for p in passports if validate_passport(p)])


def solve2(input_data):
    passports = parse(input_data)
    valid_passports = [p for p in passports if validate_passport(p)]
    return len([p for p in valid_passports if validate_passport_values(p)])

test_data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

invalid_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

if __name__ == "__main__":
    from aocd.models import Puzzle
    assert solve(test_data) == 2

    for passport in parse(invalid_passports):
        assert not validate_passport_values(passport)
        
    for passport in parse(valid_passports):
        assert validate_passport_values(passport)

    puz4 = Puzzle(2020, 4)
    data = puz4.input_data
    puz4.answer_a = solve(data)
    puz4.answer_b = solve2(data)
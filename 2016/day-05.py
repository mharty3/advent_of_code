# --- Day 5: How About a Nice Game of Chess? ---
import hashlib

def solve1(door_id):
    code = []
    i = 0
    while len(code) < 8:
        s = (door_id + str(i)).encode('utf-8')
        hash = hashlib.md5(s).hexdigest()
        i += 1 
        if hash[:5] == '00000':
            code.append(hash[5])
    return ''.join(code)

print(solve1(door_id='ojvtpuvg'))

def solve2(door_id):
    code = ['-'] * 8 
    i = 0
    while '-' in code:
        s = (door_id + str(i)).encode('utf-8')
        hash = hashlib.md5(s).hexdigest()
        i += 1 
        if (hash[:5] == '00000'):
            index = int(hash[5], base=16)
            if index <= 7 and (code[index] == '-'):
                code[index] = hash[6]
    return ''.join(code)

print(solve2(door_id='ojvtpuvg'))

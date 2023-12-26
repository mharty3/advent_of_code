import hashlib

for i in range(1_000_000_000):
    to_hash = f'bgvyzdsv{i}'
    if hashlib.md5(to_hash.encode()).hexdigest()[:6] =='000000':
        print(i)
        break 
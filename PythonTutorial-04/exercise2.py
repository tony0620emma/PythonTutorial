
def xxxxx(n):
    b = bin(n)
    count = 0
    for c in b:
        if c == '1':
            count += 1
    return count

def num_of_1_bits(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n >>= 1
    return count

print(num_of_1_bits(77))
print(num_of_1_bits(3))
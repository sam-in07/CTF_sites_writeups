from string import ascii_lowercase, digits

# Your numbers
numbers = [
    104, 372, 110, 436, 262, 173, 354, 393, 351, 297, 241, 86, 
    262, 359, 256, 441, 124, 154, 165, 165, 219, 288, 42
]

# Alphabet mapping: space + letters + digits + underscore
alphabet = ' ' + ascii_lowercase + digits + '_'

# Modular inverse function
def modinv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Decode the flag
flag = ''
for n in numbers:
    idx = modinv(n % 41, 41)
    flag += alphabet[idx]

print(flag)
from string import ascii_uppercase, digits

numbers = [
    165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138
]

alphabet = ascii_uppercase + digits + '_'

flag = ''

for n in numbers:
    flag += alphabet[n % 37]

print(flag)


# picoCTF{R0UND_N_R0UND_B6B25531}
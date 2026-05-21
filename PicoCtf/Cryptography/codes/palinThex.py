# Given plaintext in decimal
plaintext_decimal = 218378661235194013475375491560393839271890611748313869466505982182725236291814729136509

# Convert to hexadecimal
plaintext_hex = hex(plaintext_decimal)[2:]  # Remove the '0x' prefix

# Convert hexadecimal to ASCII (decode from hex to bytes and then decode bytes to string)
try:
    plaintext_ascii = bytes.fromhex(plaintext_hex).decode('utf-8')
except UnicodeDecodeError:
    plaintext_ascii = "Invalid ASCII (non-printable characters or encoding error)"

# Print results
print("Hexadecimal:", plaintext_hex)
print("ASCII:", plaintext_ascii)
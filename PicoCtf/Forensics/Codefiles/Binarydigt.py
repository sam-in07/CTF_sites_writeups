# Binarydigt.py

import os

# Full path to your digits.bin
bin_path = "/home/samin/Downloads/Picofiles/digits.bin"

# Output file (in the same folder as digits.bin)
output_path = "/home/samin/Downloads/Picofiles/recovered.jpg"

# Read the binary data
with open(bin_path, "r") as f:
    bits = f.read().strip()

# Convert every 8 bits into a byte / one byte 
data = bytes(
    int(bits[i:i+8], 2)
    for i in range(0, len(bits), 8)
    if len(bits[i:i+8]) == 8
)

# Write to a JPEG file
with open(output_path, "wb") as f:
    f.write(data)

print("wrote", len(data), "bytes")
print(f"recovered.jpg saved to {output_path}")
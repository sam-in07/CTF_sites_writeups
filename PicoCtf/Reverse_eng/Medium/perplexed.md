https://learn.cylabacademy.org/library/458

Ans :

https://prasanth26.medium.com/picoctf-perplexed-writeup-11a7e7296893

```c++
undefined8 check(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  size_t sVar3;
  char local_58 [36];
  uint local_34;
  uint local_30;
  undefined4 local_2c;
  int local_28;
  uint local_24;
  int local_20;
  int local_1c;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 27) {
    local_58[0] = -0x1f;
    local_58[1] = -0x59;
    local_58[2] = '\x1e';
    local_58[3] = -8;
    local_58[4] = 'u';
    local_58[5] = '#';
    local_58[6] = '{';
    local_58[7] = 'a';
    local_58[8] = -0x47;
    local_58[9] = -99;
    local_58[10] = -4;
    local_58[0xb] = 'Z';
    local_58[0xc] = '[';
    local_58[0xd] = -0x21;
    local_58[0xe] = 'i';
    local_58[0xf] = 0xd2;
    local_58[0x10] = -2;
    local_58[0x11] = '\x1b';
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 'g';
    local_58[0x16] = -0xc;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;
    for (local_24 = 0; local_24 < 0x17; local_24 = local_24 + 1) {
      for (local_28 = 0; local_28 < 8; local_28 = local_28 + 1) {
        if (local_20 == 0) {
          local_20 = 1;
        }
                local_30 = 1 << (7U - (char)local_28 & 31);
        local_34 = 1 << (7U - (char)local_20 & 31);;
        if (0 < (int)((int)param_1[local_1c] & local_34) !=
            0 < (int)((int)local_58[(int)local_24] & local_30)) {
          return 1;
        }
        local_20 = local_20 + 1;
        if (local_20 == 8) {
          local_20 = 0;
          local_1c = local_1c + 1;
        }
        sVar3 = (size_t)local_1c;
        sVar1 = strlen(param_1);
        if (sVar3 == sVar1) {
          return 0;
        }
      }
    }
    uVar2 = 0;
  }
  else {
    uVar2 = 1;
  }
  return uVar2;
}


```



 if (sVar1 == 27) 27 bit 


     local_58[0] = '\xe1';
    local_58[1] = '\xa7';
    local_58[2] = '\x1e';
    local_58[3] = '\xf8';
    local_58[4] = 0x75;
    local_58[5] = 0x23;
    local_58[6] = 0x7b;
    local_58[7] = 0x61;
    local_58[8] = '\xb9';
    local_58[9] = '\x9d';
    local_58[10] = '\xfc';
    local_58[0xb] = 0x5a;
    local_58[0xc] = 0x5b;
    local_58[0xd] = '\xdf';
    local_58[0xe] = 0x69;
    local_58[0xf] = 0xd2;
    local_58[0x10] = '\xfe';
    local_58[0x11] = 0x1b;
    local_58[0x12] = -0x13;
    local_58[0x13] = -0xc;
    local_58[0x14] = -0x13;
    local_58[0x15] = 0x67;
    local_58[0x16] = -0xc;
    local_1c = 0;
    local_20 = 0;
    local_2c = 0;

     "\xe1\xa7\x1e\xf8\x75\x23\x7b\x61\xb9\x9d\xfc\x5a\x5b\xdf\x69\xd2\xfe\x1b\xed\xf4\xed\x67\xf4", 




```python
secret = bytes([
    0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61,
    0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2,
    0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4
])

# Convert to a bit string
bitstream = ''.join(f'{b:08b}' for b in secret)

# Split into 7-bit chunks 
chunks = [bitstream[i:i+7] for i in range(0, len(bitstream), 7)]

# Convert each chunk into ASCII
password = ''.join(chr(int(c, 2)) for c in chunks)

print("Recovered password:", password)
print("Length:", len(password))
```

Recovered password: picoCTF{0n3_bi7_4t_a_7im3}
Length: 27








This code is taking a sequence of raw bytes, turning them into a continuous stream of bits, splitting that stream into 7-bit pieces, and then interpreting each 7-bit piece as an ASCII character to reconstruct a “password.”

Here’s what each part is doing step by step:

---

### 1. Raw byte data

```python
secret = bytes([
    0xe1, 0xa7, 0x1e, 0xf8, 0x75, 0x23, 0x7b, 0x61,
    0xb9, 0x9d, 0xfc, 0x5a, 0x5b, 0xdf, 0x69, 0xd2,
    0xfe, 0x1b, 0xed, 0xf4, 0xed, 0x67, 0xf4
])
```

This is a byte array (23 bytes total). Each value is an 8-bit number (0–255).

---

### 2. Convert bytes to a bit string

```python
bitstream = ''.join(f'{b:08b}' for b in secret)
```

Each byte is converted into its 8-bit binary representation.

Example:

* `0xe1` → `11100001`
* `0xa7` → `10100111`

Then all of them are concatenated into one long string of bits.

So instead of 23 separate bytes, you now have:

```
23 × 8 = 184 bits total
```

---

### 3. Split into 7-bit chunks

```python
chunks = [bitstream[i:i+7] for i in range(0, len(bitstream), 7)]
```

Now the 184-bit stream is cut into chunks of 7 bits each.

Important note:

* ASCII traditionally uses **7-bit encoding**, so this is trying to interpret the data as 7-bit ASCII characters.

However:

* 184 ÷ 7 = 26 full chunks with 2 leftover bits (incomplete chunk at the end)

So the last chunk may be shorter or invalid.

---

### 4. Convert each 7-bit chunk to a character

```python
password = ''.join(chr(int(c, 2)) for c in chunks)
```

For each chunk:

1. Convert binary string → integer (`int(c, 2)`)
2. Convert integer → ASCII character (`chr(...)`)
3. Join everything into a final string

So something like:

```
"1000001" → 65 → 'A'
```

---

### 5. Output

```python
print("Recovered password:", password)
print("Length:", len(password))
```

This prints:

* The decoded string (“password”)
* Its length (number of 7-bit characters produced)

---

## ⚠️ Key idea behind this code

This is a **bit-level decoding trick**, often seen in:

* CTF (capture-the-flag) challenges
* Steganography
* custom encodings

It assumes:

> “The original message was packed into 7-bit ASCII, then stored as 8-bit bytes.”

---

## ⚠️ Potential issue in this code

Because:

* 184 bits is not divisible by 7

You may get:

* a final incomplete chunk
* garbage character at the end
* or decoding error depending on input handling

---

## In one sentence

This code takes encrypted-looking bytes, converts them into a binary stream, splits them into 7-bit ASCII units, and reconstructs a hidden text string from those bits.

---

If you want, I can also decode this exact byte sequence and show you what the output actually becomes.

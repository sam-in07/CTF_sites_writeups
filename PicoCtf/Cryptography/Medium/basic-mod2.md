Problem : https://learn.cylabacademy.org/library/125  

A new modular challenge!

Download the message here (PicoCtf/Cryptography/Medium/files/basic-mod2/message.txt)

.

Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.

Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})


Soln :
PicoCtf/Cryptography/codes/basic-mod2/code.py



┌──(samin㉿kali)-[~/…/PicoCtf/Cryptography/codes/basic-mod2]
└─$ python3 code.py
1nv3r53ly_h4rd_dadaacaa
                             



```python

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
```



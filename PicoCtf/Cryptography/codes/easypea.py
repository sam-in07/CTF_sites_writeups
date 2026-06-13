from pwn import *

enc_flag = bytes.fromhex("73e7a714676a81d9bd03339392733c7af01ccb2cdd9dd3d0dac14f90655b79db")
enc_text = bytes.fromhex("f7f0ff4d11f53afbece96cfc980c4cf382340284808ebfc13cf77741860abf60ea949399b2579325d15de133179b37e7bdf6d0a524dddff85342692645eea703")

known_plain = b'A' * len(enc_text)

key = xor(enc_text, known_plain)

flag = xor(enc_flag, key[:len(enc_flag)])

print(flag)






from pwn import *

KEY_LEN = 50000

p = remote("mercury.picoctf.net", 11188)

p.recvuntil(b"flag!\n")
enc_flag = p.recvline().strip()
enc_flag_len = len(enc_flag) // 2       # 32

to_enc = b"A" * (KEY_LEN-enc_flag_len)
p.sendlineafter(b"encrypt? ", to_enc)

# now enc flag...
p.sendlineafter(b"encrypt? ", bytes.fromhex(enc_flag.decode()))
p.recvline()
flag = p.recvline().strip()

print(b"picoCTF{" + bytes.fromhex(flag.decode()) + b"}")

# picoCTF{7904ff830f1c5bba8f763707247ba3e1}
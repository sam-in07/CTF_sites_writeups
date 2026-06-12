https://learn.cylabacademy.org/library/256  

PicoCtf/Reverse_eng/Medium/Files/bloatpy 


soln : 

```python


import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
  else:
    print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
    # sys.exit(0)
    return False
def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])
def arg232():
  return input(a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94])
def arg132():
  return open('flag.txt.enc', 'rb').read()
def arg112():
  print(a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25])
def arg122(arg432, arg423):
    arg433 = arg423
    i = 0
    while len(arg433) < len(arg432):
        arg433 = arg433 + arg423[i]
        i = (i + 1) % len(arg423)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
arg444 = arg132()
arg432 = arg232()
arg133(arg432)
arg112()
arg423 = arg111(arg444)
print(arg423)
sys.exit(0)


```

Please enter correct password for flag: 
That password is incorrect
Welcome back... your flag, user:
picoCTF{d30bfu5c4710n_f7w_161a4f09}
                                                                                                   








====================



Because commenting out `sys.exit(0)` changes the program's control flow.

Let's look at the important part:

```python
def arg133(arg432):
  if arg432 == "..." :   # correct password
    return True
  else:
    print("That password is incorrect")
    # sys.exit(0)
    return False
```

Originally, it was probably:

```python
else:
    print("That password is incorrect")
    sys.exit(0)
```

### What `sys.exit(0)` does

`sys.exit(0)` immediately terminates the program.

So with it enabled:

1. User enters wrong password.
2. `arg133()` prints "That password is incorrect".
3. `sys.exit(0)` stops execution.
4. The code below never runs.

---

### What happens after you comment it out

Now the function does:

```python
else:
    print("That password is incorrect")
    return False
```

But notice the caller ignores the return value:

```python
arg444 = arg132()
arg432 = arg232()
arg133(arg432)      # return value not checked
arg112()
arg423 = arg111(arg444)
print(arg423)
```

Even if `arg133()` returns `False`, the program continues.

So:

1. Wrong password entered.
2. Error message printed.
3. Program keeps running.
4. Encrypted file is read.
5. `arg111()` decrypts it.
6. The decrypted contents (the flag) are printed.

A more correct implementation would have been:

```python
if not arg133(arg432):
    sys.exit(0)
```

or

```python
if arg133(arg432):
    arg112()
    arg423 = arg111(arg444)
    print(arg423)
```

### Why the flag is still decrypted

The password is **not actually used to decrypt the flag**.

The decryption key is hardcoded:

```python
def arg111(arg444):
    return arg122(arg444.decode(), "ralscallion")
```

The program always decrypts using the fixed string `"ralscallion"` (after decoding the character-array obfuscation). The password check is only a gate that was supposed to stop execution.

So by removing:

```python
sys.exit(0)
```

you bypass the gate, and the program happily decrypts and prints the flag anyway.

This is a common beginner-level reverse-engineering/CTF mistake: the secret is protected only by a client-side check, while the decryption key is embedded in the code itself.


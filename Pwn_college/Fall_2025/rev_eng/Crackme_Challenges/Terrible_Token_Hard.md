# Terrible Token Hard — Reverse Engineering Walkthrough

## Challenge

Binary:

```bash
/challenge/terrible-token-hard
```

The goal is to reverse engineer the license verification logic and determine the correct 5-byte license key.

---

## 1. Initial Investigation with `strings`

Run:

```bash
strings /challenge/terrible-token-hard
```

Among the output, there is a notable 5-character printable string:

```text
iyjwt
```

The binary also contains the normal license-verifier strings:

```text
Checking the received license key!
Wrong! No flag for you!
You win! Here is your flag:
/flag
```

The `iyjwt` string is therefore a strong candidate for the expected license value.

---

## 2. Inspecting the Program with `ltrace`

Run:

```bash
ltrace /challenge/terrible-token-hard
```

The important part of the output is:

```text
read(0, "\n", 5) = 1
...
puts("Checking the received license ke"...Checking the received license key!)
...
memcmp(0x7ffc1593a342, 0x5f90fc778010, 5, ...) = 0xffffffa1
...
puts("Wrong! No flag for you!"Wrong! No flag for you!)
```

This tells us:

* The program reads at most **5 bytes** from standard input.
* The program checks the license using `memcmp()`.
* `memcmp()` compares exactly **5 bytes**.
* There is no visible mangling step between reading the input and the comparison.

---

## 3. No Mangling Operation

This challenge differs from `tangled-ticket-easy` and `tangled-ticket-hard`.

Those challenges explicitly described transformations such as:

```text
swap indexes 1 and 4
```

or required inspecting transformed buffers.

Here, the program goes directly from:

```text
Ready to receive your license key!
```

to:

```text
Checking the received license key!
```

and then:

```text
memcmp(..., ..., 5)
```

There is no message indicating a swap, XOR, reversal, or other transformation.

Therefore, the 5-byte printable value embedded in the binary can be used directly as the license key.

---

## 4. Determining the License

The candidate value found with `strings` is:

```text
iyjwt
```

It contains exactly five characters:

```text
i y j w t
```

This matches the 5-byte length used by:

```text
memcmp(..., ..., 5)
```

Therefore:

```text
Expected license:
iyjwt
```

---

## 5. Verification

Test the candidate with:

```bash
printf 'iyjwt' | /challenge/terrible-token-hard
```

Alternatively:

```bash
echo 'iyjwt' | /challenge/terrible-token-hard
```

The important point is that the input is exactly five characters:

```text
i y j w t
```

which matches the expected 5-byte comparison.

---

## 6. Why `strings` Is Enough Here

The binary exposes the expected token as a printable string:

```text
iyjwt
```

Unlike a challenge where the expected value is encoded or transformed, there is no additional mangling logic indicated by the program output.

The `ltrace` result confirms the comparison length:

```text
memcmp(..., ..., 5)
```

So the evidence lines up:

```text
strings:
iyjwt
   ↓
5 characters

ltrace:
memcmp(..., ..., 5)
   ↓
5-byte comparison

No mangling:
   ↓
use the value directly
```

---

## 7. Final Solution

The correct license key is:

```text
iyjwt
```

Verification command:

```bash
printf 'iyjwt' | /challenge/terrible-token-hard
```

### Summary

| Observation          | Result                           |
| -------------------- | -------------------------------- |
| Binary               | `/challenge/terrible-token-hard` |
| Input size           | 5 bytes                          |
| Comparison           | `memcmp(..., ..., 5)`            |
| Mangling             | None observed                    |
| Token from `strings` | `iyjwt`                          |
| License key          | **`iyjwt`**                      |


## hacker@reverse-engineering~terrible-token-hard:~$ gdb -q /challenge/terrible-token-hard
```json
Reading symbols from /challenge/terrible-token-hard...
(No debugging symbols found in /challenge/terrible-token-hard)
(gdb) break memcmp
Breakpoint 1 at 0x1170
(gdb) run
Starting program: /challenge/terrible-token-hard 
###
### Welcome to /challenge/terrible-token-hard!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

cccccccccccccccccccccc
Checking the received license key!


Breakpoint 1.1, __memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:43
warning: 43     ../sysdeps/x86_64/multiarch/memcmp-sse4.S: No such file or directory
(gdb) ccccccccccccccccc
Undefined command: "ccccccccccccccccc".  Try "help".
(gdb) x/5bx $rdi
0x7fff216585b2: 0x63    0x63    0x63    0x63    0x63
(gdb) x/5bx $rsi
0x5e1c520d7010: 0x69    0x79    0x6a    0x77    0x74
(gdb) quit 
```


``
I found the expected 5 bytes:

```text
69 79 6a 77 74
```

Converting those hex values to ASCII:

```text
69 = i
79 = y
6a = j
77 = w
74 = t
```

So the license key is:

```text
iyjwt
```

Exit GDB with:

```bash
quit
```

Then run:

```bash
printf 'iyjwt' | /challenge/terrible-token-hard
`````

That should give you the flag.



hacker@reverse-engineering~terrible-token-hard:~$ printf 'iyjwt' | /challenge/terrible-token-hard


###
### Welcome to /challenge/terrible-token-hard!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Checking the received license key!

You win! Here is your flag:
## pwn.college{EZXk_7Zj60EbTvjdSaJha5lJksZ.dJTNywSM2QDN4EzW}


hacker@reverse-engineering~terrible-token-hard:~$ 



<img src="images/ter_hard.png" alt="Description" style="width:200%;">
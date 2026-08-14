# Terrible Token Easy — Reverse Engineering Walkthrough

## Challenge

Binary:

```bash
/challenge/terrible-token-easy
```

The goal is to reverse engineer the license verification logic and determine the correct 5-byte license key.

---

## 1. Initial Investigation

Run the binary:

```bash
/challenge/terrible-token-easy
```

The program asks for a license key and displays the bytes it receives.

With an empty/newline input, the output shows:

```text
Initial input:

    0a 00 00 00 00

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

    0a 00 00 00 00

Expected result:

    79 78 66 75 63
```

The important observation is that the **initial input and final mangled input are identical**.

Therefore, this challenge does not perform any transformation on the input.

---

## 2. Finding the Expected Bytes

The expected result is:

```text
79 78 66 75 63
```

Convert each hexadecimal byte to ASCII:

```text
79 = y
78 = x
66 = f
75 = u
63 = c
```

Therefore:

```text
yxfuc
```

is the expected 5-byte value.

---

## 3. Confirming with `ltrace`

Run:

```bash
ltrace /challenge/terrible-token-easy
```

The important section is:

```text
Expected result:

printf("%02x ", 0x7979)
printf("%02x ", 0x7878)
printf("%02x ", 0x6666)
printf("%02x ", 0x7575)
printf("%02x ", 0x6363)
```

The values correspond to:

```text
79 78 66 75 63
```

which is:

```text
yxfuc
```

The program also calls:

```text
memcmp(..., ..., 5, ...)
```

so exactly 5 bytes are compared.

---

## 4. Checking for a Mangling Operation

Unlike challenges such as `tangled-ticket-easy`, there is no message describing a swap, XOR, reversal, or other transformation.

More importantly, the program explicitly demonstrates that the mangling stage leaves the input unchanged:

```text
Initial input:
    0a 00 00 00 00

Final result of mangling input:
    0a 00 00 00 00
```

Therefore:

```text
Input
  ↓
No transformation
  ↓
Final comparison value
```

The required input is simply the expected value.

---

## 5. Confirmation with `strings`

Running:

```bash
strings /challenge/terrible-token-easy
```

reveals:

```text
yxfuc
```

This is another strong indication that `yxfuc` is embedded directly in the binary as the expected license value.

The binary also contains:

```text
EXPECTED_RESULT
```

which suggests that the expected comparison value is stored as a global/static value.

---

## 6. Solving the Challenge

The complete reasoning is:

```text
Expected bytes:
79 78 66 75 63

Convert to ASCII:
y x f u c

Expected result:
yxfuc

Mangling:
none

Required license:
yxfuc
```

There is no need to reverse a transformation because the mangled result is identical to the original input.

---

## 7. Verifying the License

Run:

```bash
printf 'yxfuc' | /challenge/terrible-token-easy
```

The program should now accept the license and proceed to the flag-reading code.

---

## Final Answer

The correct license key is:

```text
yxfuc
```

### Summary

| Step           | Result                |
| -------------- | --------------------- |
| Input length   | 5 bytes               |
| Mangling       | None                  |
| Expected bytes | `79 78 66 75 63`      |
| Expected ASCII | `yxfuc`               |
| License key    | **`yxfuc`**           |
| Verification   | `memcmp(..., ..., 5)` |



## hacker@reverse-engineering~terrible-token-easy:~$ printf 'yxfuc' | /challenge/terrible-token-easy
```json

###
### Welcome to /challenge/terrible-token-easy!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Initial input:

        79 78 66 75 63 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        79 78 66 75 63 

Expected result:

        79 78 66 75 63 

Checking the received license key!

You win! Here is your flag:
pwn.college{4TgdDujNwY2Yn7DaLvzA1sOvdDp.dFTNywSM2QDN4EzW}


```


## You’ve already reverse-engineered the important part. The key is **`yxfuc`**.

Why:

* The program reads **5 bytes**.
* Your `ltrace` shows `memcmp(..., 5)`.
* The mangling appears to leave the input unchanged.
* Expected bytes are:

```text
79 78 66 75 63
```

Those hex bytes translate to:

```text
79 = y
78 = x
66 = f
75 = u
63 = c
```

So provide exactly `yxfuc`.

Because the program reads exactly 5 bytes, use:

```bash
printf 'yxfuc' | /challenge/terrible-token-easy
```

You should get the flag.

<img src="images/ter_easy.png" alt="Description" style="width:200%;">
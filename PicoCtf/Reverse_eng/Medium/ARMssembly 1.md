https://learn.cylabacademy.org/library/111

For what argument does this program print "win"?

Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

Variables: a = 86, b = 3, c = 3


Ans :


The assembly you've posted does, by itself, requires the input **469**. Here's the math again:

```c
88 << 4 = 1408
1408 / 3 = 469    // integer division
return 469 - input;
```

`main` prints **"You win!"** only if the return value is zero:

```c
if (func(input) == 0)
    puts("You win!");
```

So the required input is:

```
469 (decimal)
= 0x1d5
= 000001d5 (32-bit hex)
```

If `picoCTF{000001d5}` is rejected, then the assembly you've pasted does **not** match the binary that generated the flag.

I also noticed your message says:

> Variables: **a = 86, b = 3, c = 3**

but the assembly clearly hardcodes

```
88
4
3
```

Those values don't match. Many picoCTF reversing challenges generate a unique binary per player, and those `a`, `b`, `c` values are usually what you should use.

Could you either:

1. upload the actual binary (`chall_1`), **or**
2. paste the assembly generated from **your** binary (with the constants matching `a=86, b=3, c=3`)?

With the values `a=86, b=3, c=3`, the computation would instead be:

```
(86 << 3) / 3 = 688 / 3 = 229
```

which would make the input **229** (`000000e5`), **if** the code is otherwise identical.



000000e5
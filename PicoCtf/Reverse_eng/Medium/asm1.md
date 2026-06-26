
https://learn.cylabacademy.org/library/20

Soln : 


![**Medium\images\asm1.png**](https://github.com/sam-in07/CTF_sites_writeups/blob/saminnn/PicoCtf/Reverse_eng/Medium/images/asm1.png)



Evaluate the function with input `0x295`.

Step by step:

1. Compare `0x295` with `0x3ff`:

   * `0x295` (661) is **not greater** than `0x3ff` (1023), so do **not** jump to `+41`.

2. Compare `0x295` with `0x295`:

   * They are **equal**, so `jne` is **not** taken.

3. Execute:

   ```asm
   mov eax, [ebp+0x8]
   add eax, 0xd
   ```

   So:

   ```
   eax = 0x295 + 0xd = 0x2a2
   ```

4. The function returns `eax`.

**Answer:**

```text
0x2a2
```

Link : https://learn.cylabacademy.org/library/397

Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.

Debug this (PicoCtf/Reverse_eng/Medium/Files/debugger0_c)
.

soln : 



Just like in the previous problem, we want to pause program execution after a certain instruction has executed, but this time we want to examine memory instead of a register.

    Set a breakpoint after the constant is written.
    Run the program.
    Examine memory like so: (gdb) x/4xb $rbp-0x4

You’ll notice that the bytes are in reverse order. This is called little endian and it means that for any given number, the least significant bytes are written first. Big endian is the opposite, and this is what is more natural to people, the most significant bytes are written first. Little endianness is an aspect of the particular assembly language we are using: x86-64.


https://www.stackzero.net/gdb-baby-step-3/  
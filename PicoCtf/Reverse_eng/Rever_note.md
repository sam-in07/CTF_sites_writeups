cat disassembler-dump0_c.txt

rsp, rbp, rsi, rdi — 64 bit register
esp, ebp, esi, edi — 32 bit register
bx, cx, dx— 16 bit register
DWORD — 32 bit / 4 byte
QWORD — 64 bit / 8 byte

   file x 
 **chmod +x run  (for execute permission)
 ./run  ** (mandatory naile run hobe na code )


gdb -q x    run   info functions   
 set disassembly-flavor intel (But before we continue, we should remember that GDB uses AT&T by default, so we need to convert it to intel:)

 disassemble main 

 print hex_val (0xXXXXXX)

  break main  
  
  layout asm (This displays a window within GDB that shows the assembly code of the program being debugged, which is very useful for understanding how instructions are executed at the processor level while the program is running.)  then cmd : run 

  break *hex_val

  info registers rip  (Note that this command will continue running the program until it reaches the breakpoint and you can always know where your code stopped running via the EIP register or RIP register in x64 because it always contains the memory address of the instruction that will be executed:)

   print $eax (loc question jeta bolbe)


strings -t x XX.class | grep picoCTF
















Reverse Engineering (Rev) is the process of analyzing a compiled binary to understand its logic and retrieve a hidden flag. Binary Exploitation (Pwn) involves finding and abusing software vulnerabilities (like buffer overflows) to hijack control of the program and execute arbitrary code



Reverse Engineering (Rev)The Goal: Disassemble or decompile compiled machine code back into readable logic (like pseudocode) to figure out exactly what the program expects.Key Tasks: Figuring out custom encryption algorithms, reconstructing data structures, and bypassing DRM or license checks.The "Flag": Usually found by reversing the logic to determine the correct password/input or decrypting a stored secret.Common Tools: Ghidra, IDA Pro, Binary Ninja.Skills Needed: Deep knowledge of assembly (x86/x64/ARM), C/C++ data types, and debugging.



Rule : read the code understand what want then step into next Happy flag!!!!!!!1
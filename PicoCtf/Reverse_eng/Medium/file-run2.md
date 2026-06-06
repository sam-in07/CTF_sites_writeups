Link : https://learn.cylabacademy.org/library/267

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?

Download the program here(PicoCtf/Reverse_eng/Medium/file-run2.md)


Soln : 

┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ chmod +x run2             
                                                                                                                                   
┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ ./run2 hellw  
Won't you say 'Hello!' to me first?
                                                                                                                                   
┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ ./run2 Hello!    
The flag is: **pico{F1r57_4rgum3n7_f65ed63e}     **                                                                                                



┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/Files]
└─$ ./run2 Hello! | cut -d " " -f4

**picoCTF{F1r57_4rgum3n7_f65ed63e}**







==============================================================

Step 1: strcmp(*(char **)(param_2 + 8), "Hello!")
param_2: This is presumably a pointer to some structure or array in memory.
param_2 + 8: Moves 8 bytes ahead from param_2. In C, adding an integer to a pointer adds that many bytes if it’s a char*, or multiples of sizeof(type) if it’s a typed pointer.
If param_2 is a char*, then param_2 + 8 points 8 bytes ahead.
If param_2 is a struct pointer, this is likely accessing the third 4-byte field (on a 32-bit system) or second field (on 64-bit), depending on architecture.
*(char **)(param_2 + 8): Interprets that memory as a char* and dereferences it.
So effectively, you are reading a pointer to a string stored at param_2 + 8.
strcmp(..., "Hello!"): Compares the string at that pointer to "Hello!".
strcmp returns:
0 if the strings are equal
<0 if the first string is less than the second
>0 if the first string is greater than the second
Step 2: if (iVar1 == 0)
If the comparison returns 0 (strings are equal), then the code executes the block inside the if.
Step 3: printf("The flag is: %s", flag);
Prints the contents of the variable flag.
This is probably some secret string or password used in CTFs or challenges.
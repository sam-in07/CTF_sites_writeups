hacker@reverse-engineering~monstrous-mangler-easy:~$ strings /challenge/monstrous-mangler-easy
/lib64/ld-linux-x86-64.so.2
mgUa
libc.so.6
exit
puts
putchar
stdin
printf
__errno_location
read
memcmp
stdout
geteuid
open
__cxa_finalize
setvbuf
strerror
__libc_start_main
write
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
You win! Here is your flag:
/flag
  ERROR: Failed to open the flag -- %s!
  Your effective user id is not 0!
  You must directly run the suid binary in order to have the correct permissions!
  ERROR: Failed to read the flag -- %s!
### Welcome to %s!
This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!
Ready to receive your license key!
Initial input:
%02x 
This challenge is now mangling your input using the `reverse` mangler.
This mangled your input, resulting in:
This challenge is now mangling your input using the `swap` mangler for indexes `22` and `35`.
This challenge is now mangling your input using the `xor` mangler with key `0x7997e425241f4a`
This challenge is now mangling your input using the `swap` mangler for indexes `2` and `32`.
This challenge is now mangling your input using the `swap` mangler for indexes `1` and `5`.
The mangling is done! The resulting bytes will be used for the final comparison.
Final result of mangling input:
Expected result:
Checking the received license key!
Wrong! No flag for you!
:*3$"
A/{!
C@h;
GLi%
UAi<
Eh@N
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
babyrev-level-8-0.c
flag_fd.5698
flag.5697
flag_length.5699
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
putchar@@GLIBC_2.2.5
__errno_location@@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
stdout@@GLIBC_2.2.5
puts@@GLIBC_2.2.5
stdin@@GLIBC_2.2.5
write@@GLIBC_2.2.5
_edata
printf@@GLIBC_2.2.5
geteuid@@GLIBC_2.2.5
read@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
memcmp@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
setvbuf@@GLIBC_2.2.5
open@@GLIBC_2.2.5
EXPECTED_RESULT
exit@@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
strerror@@GLIBC_2.2.5
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
hacker@reverse-engineering~monstrous-mangler-easy:~$ ltrace /challenge/monstrous-mangler-easy
setvbuf(0x778d83f25980, nil, 2, 0)                                                   = 0
setvbuf(0x778d83f266a0, nil, 2, 0)                                                   = 0
puts("###"###
)                                                                          = 4
printf("### Welcome to %s!\n", "/challenge/monstrous-mangler-eas"...### Welcome to /challenge/monstrous-mangler-easy!
)                = 50
puts("###"###
)                                                                          = 4
putchar(10, 0x778d83f26723, 0, 0x778d83e47297
)                                       = 10
puts("This license verifier software w"...This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
)                                          = 120
puts("are licensed to read flag files!"...are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
)                                          = 115
puts("different operations on that inp"...different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
)                                          = 120
puts("Providing the correct license ke"...Providing the correct license key will net you the flag!

)                                          = 58
puts("Ready to receive your license ke"...Ready to receive your license key!

)                                          = 36
read(0            

hacker@reverse-engineering~monstrous-mangler-easy:~$ gdb -q /challenge/monstrous-mangler-easy
Reading symbols from /challenge/monstrous-mangler-easy...
(No debugging symbols found in /challenge/monstrous-mangler-easy)
(gdb) set disassembly-flavor intel
(gdb) break mainn
Function "mainn" not defined.
Make breakpoint pending on future shared library load? (y or [n]) n
(gdb) break main 
Breakpoint 1 at 0x13b8
(gdb) run
Starting program: /challenge/monstrous-mangler-easy 

Breakpoint 1, 0x00006028846913b8 in main ()
(gdb) disassemble main
Dump of assembler code for function main:
   0x00006028846913b0 <+0>:     endbr64
   0x00006028846913b4 <+4>:     push   rbp
   0x00006028846913b5 <+5>:     mov    rbp,rsp
=> 0x00006028846913b8 <+8>:     sub    rsp,0xa0
   0x00006028846913bf <+15>:    mov    DWORD PTR [rbp-0x84],edi
   0x00006028846913c5 <+21>:    mov    QWORD PTR [rbp-0x90],rsi
   0x00006028846913cc <+28>:    mov    QWORD PTR [rbp-0x98],rdx
   0x00006028846913d3 <+35>:    mov    rax,QWORD PTR fs:0x28
   0x00006028846913dc <+44>:    mov    QWORD PTR [rbp-0x8],rax
   0x00006028846913e0 <+48>:    xor    eax,eax
   0x00006028846913e2 <+50>:    mov    rax,QWORD PTR [rip+0x2c87]        # 0x602884694070 <stdin@@GLIBC_2.2.5>
   0x00006028846913e9 <+57>:    mov    ecx,0x0
   0x00006028846913ee <+62>:    mov    edx,0x2
   0x00006028846913f3 <+67>:    mov    esi,0x0
   0x00006028846913f8 <+72>:    mov    rdi,rax
   0x00006028846913fb <+75>:    call   0x602884691180 <setvbuf@plt>
   0x0000602884691400 <+80>:    mov    rax,QWORD PTR [rip+0x2c59]        # 0x602884694060 <stdout@@GLIBC_2.2.5>
   0x0000602884691407 <+87>:    mov    ecx,0x0
   0x000060288469140c <+92>:    mov    edx,0x2
   0x0000602884691411 <+97>:    mov    esi,0x0
   0x0000602884691416 <+102>:   mov    rdi,rax
   0x0000602884691419 <+105>:   call   0x602884691180 <setvbuf@plt>
   0x000060288469141e <+110>:   lea    rdi,[rip+0xce7]        # 0x60288469210c
   0x0000602884691425 <+117>:   call   0x602884691120 <puts@plt>
   0x000060288469142a <+122>:   mov    rax,QWORD PTR [rbp-0x90]
   0x0000602884691431 <+129>:   mov    rax,QWORD PTR [rax]
   0x0000602884691434 <+132>:   mov    rsi,rax
   0x0000602884691437 <+135>:   lea    rdi,[rip+0xcd2]        # 0x602884692110
--Type <RET> for more, q to quit, c to continue without paging--
   0x000060288469143e <+142>:   mov    eax,0x0
   0x0000602884691443 <+147>:   call   0x602884691140 <printf@plt>
   0x0000602884691448 <+152>:   lea    rdi,[rip+0xcbd]        # 0x60288469210c
   0x000060288469144f <+159>:   call   0x602884691120 <puts@plt>
   0x0000602884691454 <+164>:   mov    edi,0xa
   0x0000602884691459 <+169>:   call   0x602884691100 <putchar@plt>
   0x000060288469145e <+174>:   lea    rdi,[rip+0xcc3]        # 0x602884692128
   0x0000602884691465 <+181>:   call   0x602884691120 <puts@plt>
   0x000060288469146a <+186>:   lea    rdi,[rip+0xd2f]        # 0x6028846921a0
   0x0000602884691471 <+193>:   call   0x602884691120 <puts@plt>
   0x0000602884691476 <+198>:   lea    rdi,[rip+0xd9b]        # 0x602884692218
   0x000060288469147d <+205>:   call   0x602884691120 <puts@plt>
   0x0000602884691482 <+210>:   lea    rdi,[rip+0xe07]        # 0x602884692290
   0x0000602884691489 <+217>:   call   0x602884691120 <puts@plt>
   0x000060288469148e <+222>:   mov    QWORD PTR [rbp-0x30],0x0
   0x0000602884691496 <+230>:   mov    QWORD PTR [rbp-0x28],0x0
   0x000060288469149e <+238>:   mov    QWORD PTR [rbp-0x20],0x0
   0x00006028846914a6 <+246>:   mov    QWORD PTR [rbp-0x18],0x0
   0x00006028846914ae <+254>:   mov    DWORD PTR [rbp-0x10],0x0
   0x00006028846914b5 <+261>:   mov    WORD PTR [rbp-0xc],0x0
   0x00006028846914bb <+267>:   lea    rdi,[rip+0xe0e]        # 0x6028846922d0
   0x00006028846914c2 <+274>:   call   0x602884691120 <puts@plt>
   0x00006028846914c7 <+279>:   lea    rax,[rbp-0x30]
   0x00006028846914cb <+283>:   mov    edx,0x25
   0x00006028846914d0 <+288>:   mov    rsi,rax
   0x00006028846914d3 <+291>:   mov    edi,0x0
   0x00006028846914d8 <+296>:   call   0x602884691160 <read@plt>
   0x00006028846914dd <+301>:   lea    rdi,[rip+0xe10]        # 0x6028846922f4
   0x00006028846914e4 <+308>:   call   0x602884691120 <puts@plt>
--Type <RET> for more, q to quit, c to continue without paging--
   0x00006028846914e9 <+313>:   mov    edi,0x9
   0x00006028846914ee <+318>:   call   0x602884691100 <putchar@plt>
   0x00006028846914f3 <+323>:   mov    DWORD PTR [rbp-0x68],0x0
   0x00006028846914fa <+330>:   jmp    0x602884691520 <main+368>
   0x00006028846914fc <+332>:   mov    eax,DWORD PTR [rbp-0x68]
   0x00006028846914ff <+335>:   cdqe
   0x0000602884691501 <+337>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691506 <+342>:   movzx  eax,al
   0x0000602884691509 <+345>:   mov    esi,eax
   0x000060288469150b <+347>:   lea    rdi,[rip+0xdf2]        # 0x602884692304
   0x0000602884691512 <+354>:   mov    eax,0x0
   0x0000602884691517 <+359>:   call   0x602884691140 <printf@plt>
   0x000060288469151c <+364>:   add    DWORD PTR [rbp-0x68],0x1
   0x0000602884691520 <+368>:   cmp    DWORD PTR [rbp-0x68],0x24
   0x0000602884691524 <+372>:   jle    0x6028846914fc <main+332>
   0x0000602884691526 <+374>:   lea    rdi,[rip+0xbdd]        # 0x60288469210a
   0x000060288469152d <+381>:   call   0x602884691120 <puts@plt>
   0x0000602884691532 <+386>:   lea    rdi,[rip+0xdd7]        # 0x602884692310
   0x0000602884691539 <+393>:   call   0x602884691120 <puts@plt>
   0x000060288469153e <+398>:   mov    DWORD PTR [rbp-0x64],0x0
   0x0000602884691545 <+405>:   jmp    0x602884691589 <main+473>
   0x0000602884691547 <+407>:   mov    eax,DWORD PTR [rbp-0x64]
   0x000060288469154a <+410>:   cdqe
   0x000060288469154c <+412>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691551 <+417>:   mov    BYTE PTR [rbp-0x6a],al
   0x0000602884691554 <+420>:   mov    eax,0x24
   0x0000602884691559 <+425>:   sub    eax,DWORD PTR [rbp-0x64]
   0x000060288469155c <+428>:   cdqe
   0x000060288469155e <+430>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691563 <+435>:   mov    BYTE PTR [rbp-0x69],al
   0x0000602884691566 <+438>:   mov    eax,DWORD PTR [rbp-0x64]
   0x0000602884691569 <+441>:   cdqe
   0x000060288469156b <+443>:   movzx  edx,BYTE PTR [rbp-0x69]
   0x000060288469156f <+447>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691573 <+451>:   mov    eax,0x24
   0x0000602884691578 <+456>:   sub    eax,DWORD PTR [rbp-0x64]
   0x000060288469157b <+459>:   cdqe
   0x000060288469157d <+461>:   movzx  edx,BYTE PTR [rbp-0x6a]
   0x0000602884691581 <+465>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691585 <+469>:   add    DWORD PTR [rbp-0x64],0x1
   0x0000602884691589 <+473>:   cmp    DWORD PTR [rbp-0x64],0x11
   0x000060288469158d <+477>:   jle    0x602884691547 <main+407>
   0x000060288469158f <+479>:   lea    rdi,[rip+0xdc2]        # 0x602884692358
   0x0000602884691596 <+486>:   call   0x602884691120 <puts@plt>
   0x000060288469159b <+491>:   mov    edi,0x9
   0x00006028846915a0 <+496>:   call   0x602884691100 <putchar@plt>
   0x00006028846915a5 <+501>:   mov    DWORD PTR [rbp-0x60],0x0
   0x00006028846915ac <+508>:   jmp    0x6028846915d2 <main+546>
   0x00006028846915ae <+510>:   mov    eax,DWORD PTR [rbp-0x60]
   0x00006028846915b1 <+513>:   cdqe
   0x00006028846915b3 <+515>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00006028846915b8 <+520>:   movzx  eax,al
   0x00006028846915bb <+523>:   mov    esi,eax
   0x00006028846915bd <+525>:   lea    rdi,[rip+0xd40]        # 0x602884692304
   0x00006028846915c4 <+532>:   mov    eax,0x0
   0x00006028846915c9 <+537>:   call   0x602884691140 <printf@plt>
   0x00006028846915ce <+542>:   add    DWORD PTR [rbp-0x60],0x1
   0x00006028846915d2 <+546>:   cmp    DWORD PTR [rbp-0x60],0x24
--Type <RET> for more, q to quit, c to continue without paging--
   0x00006028846915d6 <+550>:   jle    0x6028846915ae <main+510>
   0x00006028846915d8 <+552>:   lea    rdi,[rip+0xb2b]        # 0x60288469210a
   0x00006028846915df <+559>:   call   0x602884691120 <puts@plt>
   0x00006028846915e4 <+564>:   lea    rdi,[rip+0xd95]        # 0x602884692380
   0x00006028846915eb <+571>:   call   0x602884691120 <puts@plt>
   0x00006028846915f0 <+576>:   movzx  eax,BYTE PTR [rbp-0x1a]
   0x00006028846915f4 <+580>:   mov    BYTE PTR [rbp-0x74],al
   0x00006028846915f7 <+583>:   movzx  eax,BYTE PTR [rbp-0xd]
   0x00006028846915fb <+587>:   mov    BYTE PTR [rbp-0x73],al
   0x00006028846915fe <+590>:   movzx  eax,BYTE PTR [rbp-0x73]
   0x0000602884691602 <+594>:   mov    BYTE PTR [rbp-0x1a],al
   0x0000602884691605 <+597>:   movzx  eax,BYTE PTR [rbp-0x74]
   0x0000602884691609 <+601>:   mov    BYTE PTR [rbp-0xd],al
   0x000060288469160c <+604>:   lea    rdi,[rip+0xd45]        # 0x602884692358
   0x0000602884691613 <+611>:   call   0x602884691120 <puts@plt>
   0x0000602884691618 <+616>:   mov    edi,0x9
   0x000060288469161d <+621>:   call   0x602884691100 <putchar@plt>
   0x0000602884691622 <+626>:   mov    DWORD PTR [rbp-0x5c],0x0
   0x0000602884691629 <+633>:   jmp    0x60288469164f <main+671>
   0x000060288469162b <+635>:   mov    eax,DWORD PTR [rbp-0x5c]
   0x000060288469162e <+638>:   cdqe
   0x0000602884691630 <+640>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691635 <+645>:   movzx  eax,al
   0x0000602884691638 <+648>:   mov    esi,eax
   0x000060288469163a <+650>:   lea    rdi,[rip+0xcc3]        # 0x602884692304
   0x0000602884691641 <+657>:   mov    eax,0x0
   0x0000602884691646 <+662>:   call   0x602884691140 <printf@plt>
   0x000060288469164b <+667>:   add    DWORD PTR [rbp-0x5c],0x1
   0x000060288469164f <+671>:   cmp    DWORD PTR [rbp-0x5c],0x24
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691653 <+675>:   jle    0x60288469162b <main+635>
   0x0000602884691655 <+677>:   lea    rdi,[rip+0xaae]        # 0x60288469210a
   0x000060288469165c <+684>:   call   0x602884691120 <puts@plt>
   0x0000602884691661 <+689>:   lea    rdi,[rip+0xd78]        # 0x6028846923e0
   0x0000602884691668 <+696>:   call   0x602884691120 <puts@plt>
   0x000060288469166d <+701>:   mov    DWORD PTR [rbp-0x58],0x0
   0x0000602884691674 <+708>:   jmp    0x602884691790 <main+992>
   0x0000602884691679 <+713>:   mov    edx,DWORD PTR [rbp-0x58]
   0x000060288469167c <+716>:   movsxd rax,edx
   0x000060288469167f <+719>:   imul   rax,rax,0xffffffff92492493
   0x0000602884691686 <+726>:   shr    rax,0x20
   0x000060288469168a <+730>:   add    eax,edx
   0x000060288469168c <+732>:   sar    eax,0x2
   0x000060288469168f <+735>:   mov    ecx,eax
   0x0000602884691691 <+737>:   mov    eax,edx
   0x0000602884691693 <+739>:   sar    eax,0x1f
   0x0000602884691696 <+742>:   sub    ecx,eax
   0x0000602884691698 <+744>:   mov    eax,ecx
   0x000060288469169a <+746>:   mov    ecx,eax
   0x000060288469169c <+748>:   shl    ecx,0x3
   0x000060288469169f <+751>:   sub    ecx,eax
   0x00006028846916a1 <+753>:   mov    eax,edx
   0x00006028846916a3 <+755>:   sub    eax,ecx
   0x00006028846916a5 <+757>:   cmp    eax,0x6
   0x00006028846916a8 <+760>:   ja     0x60288469178c <main+988>
   0x00006028846916ae <+766>:   mov    eax,eax
   0x00006028846916b0 <+768>:   lea    rdx,[rax*4+0x0]
   0x00006028846916b8 <+776>:   lea    rax,[rip+0xf0d]        # 0x6028846925cc
   0x00006028846916bf <+783>:   mov    eax,DWORD PTR [rdx+rax*1]
--Type <RET> for more, q to quit, c to continue without paging--
   0x00006028846916c2 <+786>:   cdqe
   0x00006028846916c4 <+788>:   lea    rdx,[rip+0xf01]        # 0x6028846925cc
   0x00006028846916cb <+795>:   add    rax,rdx
   0x00006028846916ce <+798>:   notrack jmp rax
   0x00006028846916d1 <+801>:   mov    eax,DWORD PTR [rbp-0x58]
   0x00006028846916d4 <+804>:   cdqe
   0x00006028846916d6 <+806>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00006028846916db <+811>:   xor    eax,0x79
   0x00006028846916de <+814>:   mov    edx,eax
   0x00006028846916e0 <+816>:   mov    eax,DWORD PTR [rbp-0x58]
   0x00006028846916e3 <+819>:   cdqe
   0x00006028846916e5 <+821>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x00006028846916e9 <+825>:   jmp    0x60288469178c <main+988>
   0x00006028846916ee <+830>:   mov    eax,DWORD PTR [rbp-0x58]
   0x00006028846916f1 <+833>:   cdqe
   0x00006028846916f3 <+835>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00006028846916f8 <+840>:   xor    eax,0xffffff97
   0x00006028846916fb <+843>:   mov    edx,eax
   0x00006028846916fd <+845>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691700 <+848>:   cdqe
   0x0000602884691702 <+850>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691706 <+854>:   jmp    0x60288469178c <main+988>
   0x000060288469170b <+859>:   mov    eax,DWORD PTR [rbp-0x58]
   0x000060288469170e <+862>:   cdqe
   0x0000602884691710 <+864>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691715 <+869>:   xor    eax,0xffffffe4
   0x0000602884691718 <+872>:   mov    edx,eax
   0x000060288469171a <+874>:   mov    eax,DWORD PTR [rbp-0x58]
   0x000060288469171d <+877>:   cdqe
--Type <RET> for more, q to quit, c to continue without paging--
   0x000060288469171f <+879>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691723 <+883>:   jmp    0x60288469178c <main+988>
   0x0000602884691725 <+885>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691728 <+888>:   cdqe
   0x000060288469172a <+890>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x000060288469172f <+895>:   xor    eax,0x25
   0x0000602884691732 <+898>:   mov    edx,eax
   0x0000602884691734 <+900>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691737 <+903>:   cdqe
   0x0000602884691739 <+905>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x000060288469173d <+909>:   jmp    0x60288469178c <main+988>
   0x000060288469173f <+911>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691742 <+914>:   cdqe
   0x0000602884691744 <+916>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691749 <+921>:   xor    eax,0x24
   0x000060288469174c <+924>:   mov    edx,eax
   0x000060288469174e <+926>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691751 <+929>:   cdqe
   0x0000602884691753 <+931>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691757 <+935>:   jmp    0x60288469178c <main+988>
   0x0000602884691759 <+937>:   mov    eax,DWORD PTR [rbp-0x58]
   0x000060288469175c <+940>:   cdqe
   0x000060288469175e <+942>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691763 <+947>:   xor    eax,0x1f
   0x0000602884691766 <+950>:   mov    edx,eax
   0x0000602884691768 <+952>:   mov    eax,DWORD PTR [rbp-0x58]
   0x000060288469176b <+955>:   cdqe
   0x000060288469176d <+957>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691771 <+961>:   jmp    0x60288469178c <main+988>
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691773 <+963>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691776 <+966>:   cdqe
   0x0000602884691778 <+968>:   movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x000060288469177d <+973>:   xor    eax,0x4a
   0x0000602884691780 <+976>:   mov    edx,eax
   0x0000602884691782 <+978>:   mov    eax,DWORD PTR [rbp-0x58]
   0x0000602884691785 <+981>:   cdqe
   0x0000602884691787 <+983>:   mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x000060288469178b <+987>:   nop
   0x000060288469178c <+988>:   add    DWORD PTR [rbp-0x58],0x1
   0x0000602884691790 <+992>:   cmp    DWORD PTR [rbp-0x58],0x24
   0x0000602884691794 <+996>:   jle    0x602884691679 <main+713>
   0x000060288469179a <+1002>:  lea    rdi,[rip+0xbb7]        # 0x602884692358
   0x00006028846917a1 <+1009>:  call   0x602884691120 <puts@plt>
   0x00006028846917a6 <+1014>:  mov    edi,0x9
   0x00006028846917ab <+1019>:  call   0x602884691100 <putchar@plt>
   0x00006028846917b0 <+1024>:  mov    DWORD PTR [rbp-0x54],0x0
   0x00006028846917b7 <+1031>:  jmp    0x6028846917dd <main+1069>
   0x00006028846917b9 <+1033>:  mov    eax,DWORD PTR [rbp-0x54]
   0x00006028846917bc <+1036>:  cdqe
   0x00006028846917be <+1038>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00006028846917c3 <+1043>:  movzx  eax,al
   0x00006028846917c6 <+1046>:  mov    esi,eax
   0x00006028846917c8 <+1048>:  lea    rdi,[rip+0xb35]        # 0x602884692304
   0x00006028846917cf <+1055>:  mov    eax,0x0
   0x00006028846917d4 <+1060>:  call   0x602884691140 <printf@plt>
   0x00006028846917d9 <+1065>:  add    DWORD PTR [rbp-0x54],0x1
   0x00006028846917dd <+1069>:  cmp    DWORD PTR [rbp-0x54],0x24
   0x00006028846917e1 <+1073>:  jle    0x6028846917b9 <main+1033>
--Type <RET> for more, q to quit, c to continue without paging--
   0x00006028846917e3 <+1075>:  lea    rdi,[rip+0x920]        # 0x60288469210a
   0x00006028846917ea <+1082>:  call   0x602884691120 <puts@plt>
   0x00006028846917ef <+1087>:  lea    rdi,[rip+0xb1a]        # 0x602884692310
   0x00006028846917f6 <+1094>:  call   0x602884691120 <puts@plt>
   0x00006028846917fb <+1099>:  mov    DWORD PTR [rbp-0x50],0x0
   0x0000602884691802 <+1106>:  jmp    0x602884691846 <main+1174>
   0x0000602884691804 <+1108>:  mov    eax,DWORD PTR [rbp-0x50]
   0x0000602884691807 <+1111>:  cdqe
   0x0000602884691809 <+1113>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x000060288469180e <+1118>:  mov    BYTE PTR [rbp-0x6c],al
   0x0000602884691811 <+1121>:  mov    eax,0x24
   0x0000602884691816 <+1126>:  sub    eax,DWORD PTR [rbp-0x50]
   0x0000602884691819 <+1129>:  cdqe
   0x000060288469181b <+1131>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691820 <+1136>:  mov    BYTE PTR [rbp-0x6b],al
   0x0000602884691823 <+1139>:  mov    eax,DWORD PTR [rbp-0x50]
   0x0000602884691826 <+1142>:  cdqe
   0x0000602884691828 <+1144>:  movzx  edx,BYTE PTR [rbp-0x6b]
   0x000060288469182c <+1148>:  mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691830 <+1152>:  mov    eax,0x24
   0x0000602884691835 <+1157>:  sub    eax,DWORD PTR [rbp-0x50]
   0x0000602884691838 <+1160>:  cdqe
   0x000060288469183a <+1162>:  movzx  edx,BYTE PTR [rbp-0x6c]
   0x000060288469183e <+1166>:  mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x0000602884691842 <+1170>:  add    DWORD PTR [rbp-0x50],0x1
   0x0000602884691846 <+1174>:  cmp    DWORD PTR [rbp-0x50],0x11
   0x000060288469184a <+1178>:  jle    0x602884691804 <main+1108>
   0x000060288469184c <+1180>:  lea    rdi,[rip+0xb05]        # 0x602884692358
   0x0000602884691853 <+1187>:  call   0x602884691120 <puts@plt>
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691858 <+1192>:  mov    edi,0x9
   0x000060288469185d <+1197>:  call   0x602884691100 <putchar@plt>
   0x0000602884691862 <+1202>:  mov    DWORD PTR [rbp-0x4c],0x0
   0x0000602884691869 <+1209>:  jmp    0x60288469188f <main+1247>
   0x000060288469186b <+1211>:  mov    eax,DWORD PTR [rbp-0x4c]
   0x000060288469186e <+1214>:  cdqe
   0x0000602884691870 <+1216>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691875 <+1221>:  movzx  eax,al
   0x0000602884691878 <+1224>:  mov    esi,eax
   0x000060288469187a <+1226>:  lea    rdi,[rip+0xa83]        # 0x602884692304
   0x0000602884691881 <+1233>:  mov    eax,0x0
   0x0000602884691886 <+1238>:  call   0x602884691140 <printf@plt>
   0x000060288469188b <+1243>:  add    DWORD PTR [rbp-0x4c],0x1
   0x000060288469188f <+1247>:  cmp    DWORD PTR [rbp-0x4c],0x24
   0x0000602884691893 <+1251>:  jle    0x60288469186b <main+1211>
   0x0000602884691895 <+1253>:  lea    rdi,[rip+0x86e]        # 0x60288469210a
   0x000060288469189c <+1260>:  call   0x602884691120 <puts@plt>
   0x00006028846918a1 <+1265>:  lea    rdi,[rip+0xb98]        # 0x602884692440
   0x00006028846918a8 <+1272>:  call   0x602884691120 <puts@plt>
   0x00006028846918ad <+1277>:  movzx  eax,BYTE PTR [rbp-0x2e]
   0x00006028846918b1 <+1281>:  mov    BYTE PTR [rbp-0x72],al
   0x00006028846918b4 <+1284>:  movzx  eax,BYTE PTR [rbp-0x10]
   0x00006028846918b8 <+1288>:  mov    BYTE PTR [rbp-0x71],al
   0x00006028846918bb <+1291>:  movzx  eax,BYTE PTR [rbp-0x71]
   0x00006028846918bf <+1295>:  mov    BYTE PTR [rbp-0x2e],al
   0x00006028846918c2 <+1298>:  movzx  eax,BYTE PTR [rbp-0x72]
   0x00006028846918c6 <+1302>:  mov    BYTE PTR [rbp-0x10],al
   0x00006028846918c9 <+1305>:  lea    rdi,[rip+0xa88]        # 0x602884692358
   0x00006028846918d0 <+1312>:  call   0x602884691120 <puts@plt>
--Type <RET> for more, q to quit, c to continue without paging--
   0x00006028846918d5 <+1317>:  mov    edi,0x9
   0x00006028846918da <+1322>:  call   0x602884691100 <putchar@plt>
   0x00006028846918df <+1327>:  mov    DWORD PTR [rbp-0x48],0x0
   0x00006028846918e6 <+1334>:  jmp    0x60288469190c <main+1372>
   0x00006028846918e8 <+1336>:  mov    eax,DWORD PTR [rbp-0x48]
   0x00006028846918eb <+1339>:  cdqe
   0x00006028846918ed <+1341>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00006028846918f2 <+1346>:  movzx  eax,al
   0x00006028846918f5 <+1349>:  mov    esi,eax
   0x00006028846918f7 <+1351>:  lea    rdi,[rip+0xa06]        # 0x602884692304
   0x00006028846918fe <+1358>:  mov    eax,0x0
   0x0000602884691903 <+1363>:  call   0x602884691140 <printf@plt>
   0x0000602884691908 <+1368>:  add    DWORD PTR [rbp-0x48],0x1
   0x000060288469190c <+1372>:  cmp    DWORD PTR [rbp-0x48],0x24
   0x0000602884691910 <+1376>:  jle    0x6028846918e8 <main+1336>
   0x0000602884691912 <+1378>:  lea    rdi,[rip+0x7f1]        # 0x60288469210a
   0x0000602884691919 <+1385>:  call   0x602884691120 <puts@plt>
   0x000060288469191e <+1390>:  lea    rdi,[rip+0xb7b]        # 0x6028846924a0
   0x0000602884691925 <+1397>:  call   0x602884691120 <puts@plt>
   0x000060288469192a <+1402>:  movzx  eax,BYTE PTR [rbp-0x2f]
   0x000060288469192e <+1406>:  mov    BYTE PTR [rbp-0x70],al
   0x0000602884691931 <+1409>:  movzx  eax,BYTE PTR [rbp-0x2b]
   0x0000602884691935 <+1413>:  mov    BYTE PTR [rbp-0x6f],al
   0x0000602884691938 <+1416>:  movzx  eax,BYTE PTR [rbp-0x6f]
   0x000060288469193c <+1420>:  mov    BYTE PTR [rbp-0x2f],al
   0x000060288469193f <+1423>:  movzx  eax,BYTE PTR [rbp-0x70]
   0x0000602884691943 <+1427>:  mov    BYTE PTR [rbp-0x2b],al
   0x0000602884691946 <+1430>:  lea    rdi,[rip+0xa0b]        # 0x602884692358
   0x000060288469194d <+1437>:  call   0x602884691120 <puts@plt>
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691952 <+1442>:  mov    edi,0x9
   0x0000602884691957 <+1447>:  call   0x602884691100 <putchar@plt>
   0x000060288469195c <+1452>:  mov    DWORD PTR [rbp-0x44],0x0
   0x0000602884691963 <+1459>:  jmp    0x602884691989 <main+1497>
   0x0000602884691965 <+1461>:  mov    eax,DWORD PTR [rbp-0x44]
   0x0000602884691968 <+1464>:  cdqe
   0x000060288469196a <+1466>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x000060288469196f <+1471>:  movzx  eax,al
   0x0000602884691972 <+1474>:  mov    esi,eax
   0x0000602884691974 <+1476>:  lea    rdi,[rip+0x989]        # 0x602884692304
   0x000060288469197b <+1483>:  mov    eax,0x0
   0x0000602884691980 <+1488>:  call   0x602884691140 <printf@plt>
   0x0000602884691985 <+1493>:  add    DWORD PTR [rbp-0x44],0x1
   0x0000602884691989 <+1497>:  cmp    DWORD PTR [rbp-0x44],0x24
   0x000060288469198d <+1501>:  jle    0x602884691965 <main+1461>
   0x000060288469198f <+1503>:  lea    rdi,[rip+0x774]        # 0x60288469210a
   0x0000602884691996 <+1510>:  call   0x602884691120 <puts@plt>
   0x000060288469199b <+1515>:  lea    rdi,[rip+0x96e]        # 0x602884692310
   0x00006028846919a2 <+1522>:  call   0x602884691120 <puts@plt>
   0x00006028846919a7 <+1527>:  mov    DWORD PTR [rbp-0x40],0x0
   0x00006028846919ae <+1534>:  jmp    0x6028846919f2 <main+1602>
   0x00006028846919b0 <+1536>:  mov    eax,DWORD PTR [rbp-0x40]
   0x00006028846919b3 <+1539>:  cdqe
   0x00006028846919b5 <+1541>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x00006028846919ba <+1546>:  mov    BYTE PTR [rbp-0x6e],al
   0x00006028846919bd <+1549>:  mov    eax,0x24
   0x00006028846919c2 <+1554>:  sub    eax,DWORD PTR [rbp-0x40]
   0x00006028846919c5 <+1557>:  cdqe
   0x00006028846919c7 <+1559>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
--Type <RET> for more, q to quit, c to continue without paging--
   0x00006028846919cc <+1564>:  mov    BYTE PTR [rbp-0x6d],al
   0x00006028846919cf <+1567>:  mov    eax,DWORD PTR [rbp-0x40]
   0x00006028846919d2 <+1570>:  cdqe
   0x00006028846919d4 <+1572>:  movzx  edx,BYTE PTR [rbp-0x6d]
   0x00006028846919d8 <+1576>:  mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x00006028846919dc <+1580>:  mov    eax,0x24
   0x00006028846919e1 <+1585>:  sub    eax,DWORD PTR [rbp-0x40]
   0x00006028846919e4 <+1588>:  cdqe
   0x00006028846919e6 <+1590>:  movzx  edx,BYTE PTR [rbp-0x6e]
   0x00006028846919ea <+1594>:  mov    BYTE PTR [rbp+rax*1-0x30],dl
   0x00006028846919ee <+1598>:  add    DWORD PTR [rbp-0x40],0x1
   0x00006028846919f2 <+1602>:  cmp    DWORD PTR [rbp-0x40],0x11
   0x00006028846919f6 <+1606>:  jle    0x6028846919b0 <main+1536>
   0x00006028846919f8 <+1608>:  lea    rdi,[rip+0x959]        # 0x602884692358
   0x00006028846919ff <+1615>:  call   0x602884691120 <puts@plt>
   0x0000602884691a04 <+1620>:  mov    edi,0x9
   0x0000602884691a09 <+1625>:  call   0x602884691100 <putchar@plt>
   0x0000602884691a0e <+1630>:  mov    DWORD PTR [rbp-0x3c],0x0
   0x0000602884691a15 <+1637>:  jmp    0x602884691a3b <main+1675>
   0x0000602884691a17 <+1639>:  mov    eax,DWORD PTR [rbp-0x3c]
   0x0000602884691a1a <+1642>:  cdqe
   0x0000602884691a1c <+1644>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691a21 <+1649>:  movzx  eax,al
   0x0000602884691a24 <+1652>:  mov    esi,eax
   0x0000602884691a26 <+1654>:  lea    rdi,[rip+0x8d7]        # 0x602884692304
   0x0000602884691a2d <+1661>:  mov    eax,0x0
   0x0000602884691a32 <+1666>:  call   0x602884691140 <printf@plt>
   0x0000602884691a37 <+1671>:  add    DWORD PTR [rbp-0x3c],0x1
   0x0000602884691a3b <+1675>:  cmp    DWORD PTR [rbp-0x3c],0x24
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691a3f <+1679>:  jle    0x602884691a17 <main+1639>
   0x0000602884691a41 <+1681>:  lea    rdi,[rip+0x6c2]        # 0x60288469210a
   0x0000602884691a48 <+1688>:  call   0x602884691120 <puts@plt>
   0x0000602884691a4d <+1693>:  lea    rdi,[rip+0xaac]        # 0x602884692500
   0x0000602884691a54 <+1700>:  call   0x602884691120 <puts@plt>
   0x0000602884691a59 <+1705>:  lea    rdi,[rip+0xaf8]        # 0x602884692558
   0x0000602884691a60 <+1712>:  call   0x602884691120 <puts@plt>
   0x0000602884691a65 <+1717>:  mov    edi,0x9
   0x0000602884691a6a <+1722>:  call   0x602884691100 <putchar@plt>
   0x0000602884691a6f <+1727>:  mov    DWORD PTR [rbp-0x38],0x0
   0x0000602884691a76 <+1734>:  jmp    0x602884691a9c <main+1772>
   0x0000602884691a78 <+1736>:  mov    eax,DWORD PTR [rbp-0x38]
   0x0000602884691a7b <+1739>:  cdqe
   0x0000602884691a7d <+1741>:  movzx  eax,BYTE PTR [rbp+rax*1-0x30]
   0x0000602884691a82 <+1746>:  movzx  eax,al
   0x0000602884691a85 <+1749>:  mov    esi,eax
   0x0000602884691a87 <+1751>:  lea    rdi,[rip+0x876]        # 0x602884692304
   0x0000602884691a8e <+1758>:  mov    eax,0x0
   0x0000602884691a93 <+1763>:  call   0x602884691140 <printf@plt>
   0x0000602884691a98 <+1768>:  add    DWORD PTR [rbp-0x38],0x1
   0x0000602884691a9c <+1772>:  cmp    DWORD PTR [rbp-0x38],0x24
   0x0000602884691aa0 <+1776>:  jle    0x602884691a78 <main+1736>
   0x0000602884691aa2 <+1778>:  lea    rdi,[rip+0x661]        # 0x60288469210a
   0x0000602884691aa9 <+1785>:  call   0x602884691120 <puts@plt>
   0x0000602884691aae <+1790>:  lea    rdi,[rip+0xac4]        # 0x602884692579
   0x0000602884691ab5 <+1797>:  call   0x602884691120 <puts@plt>
   0x0000602884691aba <+1802>:  mov    edi,0x9
   0x0000602884691abf <+1807>:  call   0x602884691100 <putchar@plt>
   0x0000602884691ac4 <+1812>:  mov    DWORD PTR [rbp-0x34],0x0
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691acb <+1819>:  jmp    0x602884691af7 <main+1863>
   0x0000602884691acd <+1821>:  mov    eax,DWORD PTR [rbp-0x34]
   0x0000602884691ad0 <+1824>:  cdqe
   0x0000602884691ad2 <+1826>:  lea    rdx,[rip+0x2547]        # 0x602884694020 <EXPECTED_RESULT>
   0x0000602884691ad9 <+1833>:  movzx  eax,BYTE PTR [rax+rdx*1]
   0x0000602884691add <+1837>:  movzx  eax,al
   0x0000602884691ae0 <+1840>:  mov    esi,eax
   0x0000602884691ae2 <+1842>:  lea    rdi,[rip+0x81b]        # 0x602884692304
   0x0000602884691ae9 <+1849>:  mov    eax,0x0
   0x0000602884691aee <+1854>:  call   0x602884691140 <printf@plt>
   0x0000602884691af3 <+1859>:  add    DWORD PTR [rbp-0x34],0x1
   0x0000602884691af7 <+1863>:  cmp    DWORD PTR [rbp-0x34],0x24
   0x0000602884691afb <+1867>:  jle    0x602884691acd <main+1821>
   0x0000602884691afd <+1869>:  lea    rdi,[rip+0x606]        # 0x60288469210a
   0x0000602884691b04 <+1876>:  call   0x602884691120 <puts@plt>
   0x0000602884691b09 <+1881>:  lea    rdi,[rip+0xa80]        # 0x602884692590
   0x0000602884691b10 <+1888>:  call   0x602884691120 <puts@plt>
   0x0000602884691b15 <+1893>:  lea    rax,[rbp-0x30]
   0x0000602884691b19 <+1897>:  mov    edx,0x25
   0x0000602884691b1e <+1902>:  lea    rsi,[rip+0x24fb]        # 0x602884694020 <EXPECTED_RESULT>
   0x0000602884691b25 <+1909>:  mov    rdi,rax
   0x0000602884691b28 <+1912>:  call   0x602884691170 <memcmp@plt>
   0x0000602884691b2d <+1917>:  test   eax,eax
   0x0000602884691b2f <+1919>:  jne    0x602884691b45 <main+1941>
   0x0000602884691b31 <+1921>:  mov    eax,0x0
   0x0000602884691b36 <+1926>:  call   0x6028846912a9 <win>
   0x0000602884691b3b <+1931>:  mov    edi,0x0
   0x0000602884691b40 <+1936>:  call   0x6028846911a0 <exit@plt>
   0x0000602884691b45 <+1941>:  lea    rdi,[rip+0xa68]        # 0x6028846925b4
--Type <RET> for more, q to quit, c to continue without paging--
   0x0000602884691b4c <+1948>:  call   0x602884691120 <puts@plt>
   0x0000602884691b51 <+1953>:  mov    edi,0x1
   0x0000602884691b56 <+1958>:  call   0x6028846911a0 <exit@plt>
End of assembler dump.
(gdb) 
(gdb) 
(gdb) 
(gdb) 
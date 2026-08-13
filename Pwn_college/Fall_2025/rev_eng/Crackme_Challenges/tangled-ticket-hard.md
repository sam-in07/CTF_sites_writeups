## hacker@reverse-engineering~tangled-ticket-hard:~$ ltrace /challenge/tangled-ticket-hard

setvbuf(0x74025aeda980, nil, 2, 0)                                                = 0
setvbuf(0x74025aedb6a0, nil, 2, 0)                                                = 0
puts("###"###
)                                                                       = 4
printf("### Welcome to %s!\n", "/challenge/tangled-ticket-hard"### Welcome to /challenge/tangled-ticket-hard!
)                  = 47
puts("###"###
)                                                                       = 4
putchar(10, 0x74025aedb723, 0, 0x74025adfc297
)                                    = 10
puts("This license verifier software w"...This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
)                                       = 120
puts("are licensed to read flag files!"...are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
)                                       = 115
puts("different operations on that inp"...different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
)                                       = 120
puts("Providing the correct license ke"...Providing the correct license key will net you the flag!

)                                       = 58
puts("Ready to receive your license ke"...Ready to receive your license key!

)                                       = 36
read(0
, "\n", 5)                                                                  = 1
puts("Checking the received license ke"...Checking the received license key!

)                                       = 36
memcmp(0x7ffeff937642, 0x63faa19bc010, 5, 0x74025adfc297)                         = 0xffffff8a
puts("Wrong! No flag for you!"Wrong! No flag for you!
)                                                   = 24
exit(1 <no return ...>
+++ exited (status 1) +++

## hacker@reverse-engineering~tangled-ticket-hard:~$ strings /challenge/tangled-ticket-hard 

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
Checking the received license key!
Wrong! No flag for you!
:*3$"
vojov
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
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



## hacker@reverse-engineering~tangled-ticket-hard:~$ gdb -q /challenge/tangled-ticket-hard

Reading symbols from /challenge/tangled-ticket-hard...
(No debugging symbols found in /challenge/tangled-ticket-hard)
(gdb) break memcmp
Breakpoint 1 at 0x1170
(gdb) run
Starting program: /challenge/tangled-ticket-hard 
###
### Welcome to /challenge/tangled-ticket-hard!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

AAAAA
Checking the received license key!


Breakpoint 1.1, __memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:43
warning: 43     ../sysdeps/x86_64/multiarch/memcmp-sse4.S: No such file or directory
(gdb) 
(gdb) x/5bx $rdi
0x7ffcc632ea62: 0x41    0x41    0x41    0x41    0x41
(gdb) x/5bx $rdi
0x7ffcc632ea62: 0x41    0x41    0x41    0x41    0x41
(gdb) p/d $rdx
$1 = 5
(gdb) 
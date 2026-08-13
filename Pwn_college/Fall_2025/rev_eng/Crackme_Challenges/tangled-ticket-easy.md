## hacker@reverse-engineering~tangled-ticket-easy:~$  ltrace /challenge/tangled-ticket-easy

```json

setvbuf(0x74c017167980, nil, 2, 0)                                                     = 0
setvbuf(0x74c0171686a0, nil, 2, 0)                                                     = 0
puts("###"###
)                                                                            = 4
printf("### Welcome to %s!\n", "/challenge/tangled-ticket-easy"### Welcome to /challenge/tangled-ticket-easy!
)                       = 47
puts("###"###
)                                                                            = 4
putchar(10, 0x74c017168723, 0, 0x74c017089297
)                                         = 10
puts("This license verifier software w"...This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
)                                            = 120
puts("are licensed to read flag files!"...are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
)                                            = 115
puts("different operations on that inp"...different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
)                                            = 120
puts("Providing the correct license ke"...Providing the correct license key will net you the flag!

)                                            = 58
puts("Ready to receive your license ke"...Ready to receive your license key!

)                                            = 36
read(0
, "\n", 5)                                                                       = 1
puts("Initial input:\n"Initial input:

)                                                               = 16
putchar(9, 0x74c017168723, 0, 0x74c017089297    )                                          = 9
printf("%02x ", 0xa0a )                                                                   = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
puts("\n"

)                                                                             = 2
puts("This challenge is now mangling y"...This challenge is now mangling your input using the `swap` mangler for indexes `1` and `4`.

)                                            = 93
puts("This mangled your input, resulti"...This mangled your input, resulting in:

)                                            = 40
putchar(9, 0x74c017168723, 0, 0x74c017089297    )                                          = 9
printf("%02x ", 0xa0a )                                                                   = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
puts("\n"

)                                                                             = 2
puts("The mangling is done! The result"...The mangling is done! The resulting bytes will be used for the final comparison.

)                                            = 82
puts("Final result of mangling input:\n"...Final result of mangling input:

)                                           = 33
putchar(9, 0x74c017168723, 0, 0x74c017089297    )                                          = 9
printf("%02x ", 0xa0a )                                                                   = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
printf("%02x ", 000 )                                                                     = 3
puts("\n"

)                                                                             = 2
puts("Expected result:\n"Expected result:

)                                                             = 18
putchar(9, 0x74c017168723, 0, 0x74c017089297    )                                          = 9
printf("%02x ", 0x7373 )                                                                  = 3
printf("%02x ", 0x6363 )                                                                  = 3
printf("%02x ", 0x6464 )                                                                  = 3
printf("%02x ", 0x6666 )                                                                  = 3
printf("%02x ", 0x6565 )                                                                  = 3
puts("\n"

)                                                                             = 2
puts("Checking the received license ke"...Checking the received license key!

)                                            = 36
memcmp(0x7fffde76f7c2, 0x581ff0c77010, 5, 0x74c017089297)                              = 0xffffff97
puts("Wrong! No flag for you!"Wrong! No flag for you!
)                                                        = 24
exit(1 <no return ...>
+++ exited (status 1) +++
```




## hacker@reverse-engineering~tangled-ticket-easy:~$ strings /challenge/tangled-ticket-easy


```json

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
This challenge is now mangling your input using the `swap` mangler for indexes `1` and `4`.
This mangled your input, resulting in:
The mangling is done! The resulting bytes will be used for the final comparison.
Final result of mangling input:
Expected result:
Checking the received license key!
Wrong! No flag for you!
:*3$"
scdfe
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
babyrev-level-2-0.c
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
```







The key is visible from the `Expected result` and the mangling description.

### 1. Expected bytes

The output:

```text
Expected result:
    7373 6363 6464 6666 6565
```

is a little misleading because `printf("%02x ", ...)` is reading wider values. The actual expected **5 bytes** are:

```text
73 63 64 66 65
```

ASCII:

```text
s  c  d  f  e
```

So the final mangled input must be:

```text
scdfe
```

### 2. Undo the swap

The program says:

```text
using the `swap` mangler for indexes `1` and `4`
```

Assuming zero-based indexes, it swaps positions 1 and 4:

```text
Before:  s c d f e
Index:   0 1 2 3 4

Swap 1 ↔ 4:

After:   s e d f c
```

Therefore the license key you need to provide is:

```text
sedfc
```

Run it as:

```bash
printf 'sedfc' | /challenge/tangled-ticket-easy
```

If the program expects the newline as part of the input, use:

```bash
echo 'sedfc' | /challenge/tangled-ticket-easy
```

The important one is **`sedfc`**.





``hacker@reverse-engineering~tangled-ticket-easy:~$ printf 'sedfc' | /challenge/tangled-ticket-easy
###
### Welcome to /challenge/tangled-ticket-easy!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

Initial input:

        73 65 64 66 63 

This challenge is now mangling your input using the `swap` mangler for indexes `1` and `4`.

This mangled your input, resulting in:

        73 63 64 66 65 

The mangling is done! The resulting bytes will be used for the final comparison.

Final result of mangling input:

        73 63 64 66 65 

Expected result:

        73 63 64 66 65 

Checking the received license key!

You win! Here is your flag:
pwn.college{8eLElwsdyeEJnicMhOXg-f2kang.dNTNywSM2QDN4EzW}


``




<img src="images/tangled-ticket-easy.png" alt="Description" style="width:200%;">
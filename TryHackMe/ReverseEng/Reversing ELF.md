Link : https://tryhackme.com/room/reverselfiles


Soln : 

1. ┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ chmod +x crackme1          
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme1       
flag{not_that_kind_of_elf}



2. 

┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ chmod +x  crackme2
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme2
Usage: ./crackme2 password
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme2  admin
Access denied.


┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ strings crackme2                                
/lib/ld-linux.so.2
libc.so.6
_IO_stdin_used
puts
printf
memset
strcmp
__libc_start_main
/usr/local/lib:$ORIGIN
__gmon_start__
GLIBC_2.0
PTRh 
j3jA
[^_]
UWVS
t$,U
[^_]
Usage: %s password
super_secret_password
Access denied.
Access granted.
;*2$"(
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609
crtstuff.c
__JCR_LIST__
deregister_tm_clones
__do_global_dtors_aux
completed.7209
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
conditional1.c
giveFlag
__FRAME_END__
__JCR_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
strcmp@@GLIBC_2.0
_ITM_deregisterTMCloneTable
__x86.get_pc_thunk.bx
printf@@GLIBC_2.0
_edata
__data_start
puts@@GLIBC_2.0
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
__libc_csu_init
memset@@GLIBC_2.0
_fp_hw
__bss_start
main
_Jv_RegisterClasses
__TMC_END__
_ITM_registerTMCloneTable
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.jcr
.dynamic
.got.plt
.data
.bss
.comment
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme2 super_secret_password
Access granted.
flag{if_i_submit_this_flag_then_i_will_get_points}
                                                                                                        
## Easiest way :

┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ltrace ./crackme2       admin
__libc_start_main(["./crackme2", "admin"] <unfinished ...>
strcmp("admin", "super_secret_password")                                                                                                         = -1
puts("Access denied."Access denied.
)                                                                                                                           = 15
+++ exited (status 1) +++

** 
super_secret_password             **                                                                                                                            ltrace ~ compring strings (with main string and the string im giuving )   


┌──(samin㉿kali)-[~/Docume




3. 

┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ls 
crackme1  crackme2  crackme3
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ chmod +x crackme3 
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme3                      
Usage: ./crackme3 PASSWORD
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme3 ./crackme3 PASSWORD

Usage: ./crackme3 PASSWORD
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ./crackme3 PASSWORD

Come on, even my aunt Mildred got this one!
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ ltrace ./crackme3 PASSWORD   

__libc_start_main(["./crackme3", "PASSWORD"] <unfinished ...>
strlen("PASSWORD")                                                                                                                               = 8
malloc(16)                                                                                                                                       = 0x879c1e0
strlen("PASSWORD")                                                                                                                               = 8
strlen("UEFTU1dPUkQ=")                                                                                                                           = 12
puts("Come on, even my aunt Mildred go"...Come on, even my aunt Mildred got this one!
)                                                                                                      = 44
+++ exited (status 255) +++
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ strings crackme3           
/lib/ld-linux.so.2
__gmon_start__
libc.so.6
_IO_stdin_used
puts
strlen
malloc
stderr
fwrite
fprintf
strcmp
__libc_start_main
GLIBC_2.0
PTRh
iD$$
D$,;D$ 
UWVS
[^_]
Usage: %s PASSWORD
malloc failed
ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ==
Correct password!
Come on, even my aunt Mildred got this one!
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
;*2$"8
GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.ctors
.dtors
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ echo "ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ==
" |  base64 -d 
f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~/Documents/Tryhackme]
└─$ 


4.

ssh -p 2223 leviathan2@leviathan.labs.overthewire.org

ERJ9jTYWXE

soln : 



leviathan2@leviathan:~$ ls
printfile
leviathan2@leviathan:~$ ls -al
total 36
drwxr-xr-x   2 root       root        4096 Jun 24 15:01 .
drwxr-xr-x 150 root       root        4096 Jun 24 15:02 ..
-rw-r--r--   1 root       root         220 Feb 13 12:16 .bash_logout
-rw-r--r--   1 root       root        3851 Jun 24 14:50 .bashrc
-rw-r--r--   1 root       root         807 Feb 13 12:16 .profile
-r-sr-x---   1 leviathan3 leviathan2 15068 Jun 24 15:01 printfile
leviathan2@leviathan:~$ ./printfile
*** File Printer ***
Usage: ./printfile filename
leviathan2@leviathan:~$ file printfile
printfile: setuid ELF 32-bit LSB executable, Intel i386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=edf95678ff2bfd80bf9c289f61a91a378c55cfb8, for GNU/Linux 3.2.0, not stripped
leviathan2@leviathan:~$ 

leviathan2@leviathan:~$ ltrace ./printfile
__libc_start_main(["./printfile"] <unfinished ...>
puts("*** File Printer ***"*** File Printer ***
)                                                                    = 21
printf("Usage: %s filename\n", "./printfile"Usage: ./printfile filename
)                                                   = 28
+++ exited (status 255) +++




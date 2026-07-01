ssh -p 2223 leviathan.labs.overthewire.org
leviathan0


Problem : 



soln : 

leviathan0@leviathan:~$ ls 
leviathan0@leviathan:~$ la -la 
total 24
drwxr-xr-x   3 root       root       4096 Jun 24 15:01 .
drwxr-xr-x 150 root       root       4096 Jun 24 15:02 ..
drwxr-x---   2 leviathan1 leviathan0 4096 Jun 24 15:01 .backup
-rw-r--r--   1 root       root        220 Feb 13 12:16 .bash_logout
-rw-r--r--   1 root       root       3851 Jun 24 14:50 .bashrc
-rw-r--r--   1 root       root        807 Feb 13 12:16 .profile
leviathan0@leviathan:~$ cd .backup/
leviathan0@leviathan:~/.backup$ ls -la 
total 140
drwxr-x--- 2 leviathan1 leviathan0   4096 Jun 24 15:01 .
drwxr-xr-x 3 root       root         4096 Jun 24 15:01 ..
-rw-r----- 1 leviathan1 leviathan0 133259 Jun 24 15:01 bookmarks.html
leviathan0@leviathan:~/.backup$ id
uid=12000(leviathan0) gid=12000(leviathan0) groups=12000(leviathan0)
leviathan0@leviathan:~/.backup$ file bookmarks.html
bookmarks.html: HTML document, ASCII text, with very long lines (302)

leviathan0@leviathan:~/.backup$ cat bookmarks.html | grep 'pass'
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is PiXaSWQqHq" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
leviathan0@leviathan:~/.backup$ 


## PiXaSWQqHq   
the password 


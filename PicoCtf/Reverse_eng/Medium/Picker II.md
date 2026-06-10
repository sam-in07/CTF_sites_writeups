https://learn.cylabacademy.org/library/401    

Can you figure out how this program works to get the flag?

Connect to the program with netcat:

$ nc saturn.picoctf.net 54142

The program's source code can be downloaded here


Soln :
we are more restricted with a filter that checks if ‘win’ exists in the input of the user.
We can simply bypass this by directly reading the flag file which exists along the script with print(open(‘flag.txt’).read()) which would give us the flag.

┌──(samin㉿kali)-[~/…/Medium/Files/patrikparker/2no]
└─$ nc saturn.picoctf.net 64503
==> win
Illegal input
==> open('flag.txt', 'r').read
==> print(open('flag.txt', 'r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}
'NoneType' object is not callable
                                             
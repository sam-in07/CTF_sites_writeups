https://learn.cylabacademy.org/library/400 
This service can provide you with a random number, but can it do anything else?
PicoCtf/Reverse_eng/Medium/Files/picker-I.py


soln : 

Finding the Flag Function

Among the defined functions, win() stood out as it attempted to open a file named flag.txt, read its contents, and convert each character into hexadecimal before printing it. This meant I could retrieve the flag simply by executing win().


┌──(samin㉿kali)-[~/Documents/Saminsfiiles/Crf_sites_writeups]
└─$ nc saturn.picoctf.net 65275 
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d 
Try entering "getRandomNumber" without the double quotes...




picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}
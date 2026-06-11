https://learn.cylabacademy.org/library/301
Download the disk image and use mmls on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag.

Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

Download disk image(PicoCtf/Forensics/Medium/files/disk.img.gz)



soln : 

https://me-resilient64.gitbook.io/picoctf-2022-forensics/sleuthkit-intro

mmls command we can see the the partition layout 

┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ mmls disk.img                                         
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)

┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ nc saturn.picoctf.net 56506
What is the size of the Linux partition in the given disk image?
Length in sectors: 0000202752
0000202752
Great work!
picoCTF{mm15_f7w!}
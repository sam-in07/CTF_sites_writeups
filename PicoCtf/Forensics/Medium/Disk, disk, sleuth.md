https://learn.cylabacademy.org/library/113

Use srch_strings from the sleuthkit and some terminal-fu to find a flag in this disk image.

dds1-alpine.flag.img.gz  (PicoCtf/Forensics/Medium/files/dds1-alpine.flag.img.gz)



soln : 

https://medium.com/@kofikitiabi/step-by-step-guide-to-solving-disk-disk-sleuth-ii-724eeef3b0d2

┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ srch_strings dds1-alpine.flag.img | grep picoCTF
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_5e56e786}
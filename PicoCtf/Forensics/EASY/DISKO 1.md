https://learn.cylabacademy.org/library/505  


Can you find the flag in this disk image?

Download the disk image here (PicoCtf/Forensics/EASY/files/disko1/disko-1.dd.gz)

Soln : 

┌──(samin㉿kali)-[~/…/Forensics/EASY/files/disko1]
└─$ ls                 
disko-1.dd.gz
                                                                                                                  
┌──(samin㉿kali)-[~/…/Forensics/EASY/files/disko1]
└─$ gunzip disko-1.dd.gz
                                                                                                                  
┌──(samin㉿kali)-[~/…/Forensics/EASY/files/disko1]
└─$ ls 
disko-1.dd
                                                                                                                  
┌──(samin㉿kali)-[~/…/Forensics/EASY/files/disko1]
└─$ srch_strings disko-1.dd | grep picoCTF          
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}
                                      
https://learn.cylabacademy.org/library/103

Figure out how they moved the flag.

PicoCtf/Forensics/Medium/files/Trivial Flag Transfer Protocol
tftp.pcapng 

Soln : 

File => Export object => TFTP => save all 


IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS

DUEDILIGENCE ~ password 

┌──(samin㉿kali)-[~/…/Medium/files/Trivial Flag Transfer Protocol/wiresharck_export]
└─$ steghide extract -sf picture3.bmp
Enter passphrase: (DUEDILIGENCE this one is pass)
wrote extracted data to "flag.txt".

picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}

Problem : https://learn.cylabacademy.org/library/351  


How about some hide and seek heh?

Look at this image here  (PicoCtf/Cryptography/Medium/files/HideToSee/atbash.jpg)



Soln :


┌──(samin㉿kali)-[~/…/Cryptography/Medium/files/HideToSee]
└─$ steghide info atbash.jpg
"atbash.jpg":
  format: jpeg
  capacity: 2.4 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "encrypted.txt":
    size: 31.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
                                                                                                                   
┌──(samin㉿kali)-[~/…/Cryptography/Medium/files/HideToSee]
└─$ 


OR (it's best)

┌──(samin㉿kali)-[~/…/Cryptography/Medium/files/HideToSee]
└─$  steghide extract -sf atbash.jpg 
Enter passphrase: 
wrote extracted data to "encrypted.txt".

https://www.dcode.fr/atbash-cipher     

picoCTF{atbash_crack_05b2a65a}  

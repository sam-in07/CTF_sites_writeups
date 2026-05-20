link : https://learn.cylabacademy.org/library/698

Soln :

──(samin㉿kali)-[~/Downloads/Picofiles]
└─$ ls
digits.bin
                                                                                                                                                                                                                                            
┌──(samin㉿kali)-[~/Downloads/Picofiles]
└─$ file digits.bin             
digits.bin: ASCII text, with very long lines (65536), with no line terminators
                                                                                                                                                                                                                                            
┌──(samin㉿kali)-[~/Downloads/Picofiles]
└─$ head -c 100 digits.bin
1111111111011000111111111110000000000000000100000100101001000110010010010100011000000000000000010000                                                                                                                                                                                                                                            
Converting these binary bytes to hexadecimal gives:

FF D8 FF E0


python code to convert :
[PicoCtf/Forensics/Codefiles/Binarydigt.py  ](https://github.com/sam-in07/Crf_sites_writeups/blob/saminnn/PicoCtf/Forensics/Codefiles/Binarydigt.py)

┌──(samin㉿kali)-[~/…/Crf_sites_writeups/PicoCtf/Forensics/Codefiles]
└─$ python3 Binarydigt.py

┌──(samin㉿kali)-[~/Downloads/Picofiles]
└─$ xdg-open recovered.jpg


Flag Image :
![PicoCtf/Forensics/images/recovered.jpg  ](https://github.com/sam-in07/Crf_sites_writeups/blob/saminnn/PicoCtf/Forensics/images/recovered.jpg)

Flag : **picoCTF{h1dd3n_1n_th3_b1n4ry_8e65b559} **
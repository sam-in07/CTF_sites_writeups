https://learn.cylabacademy.org/library/186

Files can always be changed in a secret way. Can you find the flag?


PicoCtf/Forensics/EASY/files/cat.jpg

Soln : 

┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/EASY/files]
└─$ exiftool cat.jpg   
ExifTool Version Number         : 13.55
File Name                       : cat.jpg
Directory        

XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560

 

 cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9  

 ┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/EASY/files]
└─$ echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d 
picoCTF{the_m3tadata_1s_modified}                                                                                                                                              
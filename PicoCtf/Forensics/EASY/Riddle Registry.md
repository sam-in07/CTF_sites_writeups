https://learn.cylabacademy.org/library/530 

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.

Find the PDF file here Hidden Confidential Document
 and uncover the flag within the metadata.


 soln : 

 https://medium.com/@saumya.sriv27/riddle-registry-a-simple-picoctf-walkthrough-e221cc5cf54a


┌──(samin㉿kali)-[~/…/Forensics/EASY/files/Riddle Registry]
└─$ exiftool  confidential.pdf                                   
ExifTool Version Number         : 13.55
File Name                       : confidential.pdf
Directory                       : .
File Size                       : 183 kB
File Modification Date/Time     : 2026:06:11 23:07:47+06:00
File Access Date/Time           : 2026:06:11 23:08:18+06:00
File Inode Change Date/Time     : 2026:06:11 23:07:54+06:00
File Permissions                : -rw-rw-r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.7
Linearized                      : No
Page Count                      : 1
Producer                        : PyPDF2
Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV80MjQ0MGM3ZH0=
                                                                                                    
┌──(samin㉿kali)-[~/…/Forensics/EASY/files/Riddle Registry]
└─$ 

Author                          : cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV80MjQ0MGM3ZH0=  base64 


picoCTF{puzzl3d_m3tadata_f0und!_42440c7d}
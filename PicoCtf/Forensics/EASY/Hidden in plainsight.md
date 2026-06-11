https://learn.cylabacademy.org/library/524

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag.

Download the jpg image here
.

Soln :

┌──(samin㉿kali)-[~/…/Forensics/EASY/files/Riddle Registry]
└─$ exiftool img.jpg          
ExifTool Version Number         : 13.55
File Name                       : img.jpg
Directory                       : .
File Size                       : 73 kB
File Modification Date/Time     : 2026:06:11 23:45:46+06:00
File Access Date/Time           : 2026:06:11 23:45:51+06:00
File Inode Change Date/Time     : 2026:06:11 23:45:51+06:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
Image Width                     : 640
Image Height                    : 640
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 640x640
Megapixels                      : 0.410
                                                                                                                  
Comment                         : c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9  use base 64 decoder "cEF6endvcmQ=" this then again decode this "pAzzword"                                                                               


┌──(samin㉿kali)-[~/…/Forensics/EASY/files/Riddle Registry]
└─$ steghide extract -sf  img.jpg          
Enter passphrase: (pAzzword)
wrote extracted data to "flag.txt".
                              


picoCTF{h1dd3n_1n_1m4g3_67479645}


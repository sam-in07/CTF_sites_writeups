https://learn.cylabacademy.org/library/408

How about some hide and seek?

Download this file here (PicoCtf/Forensics/EASY/files/unknown.zip)
.

sln : 

┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/EASY/files]
└─$ exiftool  ukn_reality.jpg
ExifTool Version Number         : 13.55
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:02:16 04:40:21+06:00
File Access Date/Time           : 2026:06:11 21:42:37+06:00
File Inode Change Date/Time     : 2026:06:11 21:42:37+06:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
                                                                                                    

                                                                                                                                                                       
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/EASY/files]
└─$ echo "cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==" | base64 -d
picoCTF{ME74D47A_HIDD3N_a6df8db8}
                                                                                                                                                                       


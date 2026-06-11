https://learn.cylabacademy.org/library/114

All we know is the file with the flag is named down-at-the-bottom.txt...

dds2-alpine.flag.img.gz

soln :

https://hackpeas.medium.com/disk-disk-sleuth-ii-picoctf-wrietup-7d844944e7a5  

┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ gunzip  dds2-alpine.flag.img.gz           
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ mmls  dds2-alpine.flag.img.gz
Error stat(ing) image file (raw_open: image "dds2-alpine.flag.img.gz" - No such file or directory)
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ mmls  dds2-alpine.flag.img   
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ fls -o 2048 dds2-alpine.flag.img
d/d 26417:      home
d/d 11: lost+found
r/r 12: .dockerenv
d/d 20321:      bin
d/d 4065:       boot
d/d 6097:       dev
d/d 2033:       etc
d/d 8129:       lib
d/d 14225:      media
d/d 16257:      mnt
d/d 18289:      opt
d/d 16258:      proc
d/d 18290:      root
d/d 16259:      run
d/d 18292:      sbin
d/d 12222:      srv
d/d 16260:      sys
d/d 18369:      tmp
d/d 12223:      usr
d/d 14229:      var
V/V 32513:      $OrphanFiles
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ fls -o 2048 dds2-alpine.flag.img 18290
r/r 18291:      down-at-the-bottom.txt
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ gunzip  dds2-alpine.flag.img.gz           
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ mmls  dds2-alpine.flag.img.gz
Error stat(ing) image file (raw_open: image "dds2-alpine.flag.img.gz" - No such file or directory)
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ mmls  dds2-alpine.flag.img   
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ fls -o 2048 dds2-alpine.flag.img
d/d 26417:      home
d/d 11: lost+found
r/r 12: .dockerenv
d/d 20321:      bin
d/d 4065:       boot
d/d 6097:       dev
d/d 2033:       etc
d/d 8129:       lib
d/d 14225:      media
d/d 16257:      mnt
d/d 18289:      opt
d/d 16258:      proc
d/d 18290:      root
d/d 16259:      run
d/d 18292:      sbin
d/d 12222:      srv
d/d 16260:      sys
d/d 18369:      tmp
d/d 12223:      usr
d/d 14229:      var
V/V 32513:      $OrphanFiles
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ fls -o 2048 dds2-alpine.flag.img 18290
r/r 18291:      down-at-the-bottom.txt

                                                                                                                           The command used to retrieve this is:icat -i raw -f ext4 -o 2048 dds2-alpine.flag.img 18291icat: A tool from The Sleuth Kit (TSK) used to output the contents of a file based on its inode number.-o 2048: Specifies the partition offset.18291: The specific inode being targeted.
                                                                                                                           
                                                                                                                                
┌──(samin㉿kali)-[~/…/PicoCtf/Forensics/Medium/files]
└─$ icat -i raw -f ext4 -o 2048 dds2-alpine.flag.img 18291
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   

  picoCTF{f0r3ns1c4t0r_n0v1c3_4bd721f2}
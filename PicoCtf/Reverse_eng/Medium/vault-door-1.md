Link : https://learn.cylabacademy.org/library/12


This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java  ](https://github.com/sam-in07/CTF_sites_writeups/blob/5a02401f83b93f53b8562d23b6f6a61d4b9dd62f/PicoCtf/Reverse_eng/Medium/Files/VaultDoor1.java) 



Soln : 

Convert java to code to Py then [(PicoCtf/Reverse_eng/Medium/Files/VaultDoor1.py)](https://github.com/sam-in07/CTF_sites_writeups/blob/5a02401f83b93f53b8562d23b6f6a61d4b9dd62f/PicoCtf/Reverse_eng/Medium/Files/VaultDoor1.py)

 return (len(password) == 32 and
            password[0]  == 'd' and
            password[29] == 'a' and
            password[4]  == 'r' and
            password[2]  == '5' and
            password[23] == 'r' and
            password[3]  == 'c' and
            password[17] == '4' and
            password[1]  == '3' and
            password[7]  == 'b' and

            it's the flag element 

            then write pyhton scripts for print this words 

[PicoCtf/Reverse_eng/Medium/codefiles/vaudoosol.py](https://github.com/sam-in07/CTF_sites_writeups/blob/5a02401f83b93f53b8562d23b6f6a61d4b9dd62f/PicoCtf/Reverse_eng/Medium/codefiles/vaudoosol.py)

Run this code and found  flag 

picoCTF{}

                                                                                                                                   
┌──(samin㉿kali)-[~/…/PicoCtf/Reverse_eng/Medium/codefiles]
└─$ python3 vaudoosol.py
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_7ffa94}


Link : https://learn.cylabacademy.org/library/104


I wonder what this really is...

enc (PicoCtf/Reverse_eng/Files/enc)
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


Soln : 

灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽  decode 

we got 

54Gp5o2v5I2U5Jm744S25b2i5qW0542f5qWu542044y05pGf5r2m5by45b2i452m45iy5o2h45W9
Cg==  

https://gchq.github.io/CyberChef/#recipe=Magic(3,true,false,'')&input=54Gp5o2v5I2U5Jm744S25b2i5qW0542f5qWu542044y05pGf5r2m5by45b2i452m45iy5o2h45W9&oenc=65001  go there Paste the chines language and serach 

picoCTF{16_bits_inst34d_of_8_b7f62ca5} 
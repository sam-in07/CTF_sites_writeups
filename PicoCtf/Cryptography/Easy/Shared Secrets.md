Problem :    https://learn.cylabacademy.org/library/719

A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag?

Download the message
. And source code

PicoCtf/Cryptography/Easy/Files/Shared Secrets 

files :


Soln :

[picoCTF{dh_s3cr3t_1b25e19f}](https://medium.com/@brandynyabonyi/shared-secrets-picoctf-92286e0f4b9c)

PicoCtf/Cryptography/codes/Sharesecret/code.py

┌──(samin㉿kali)-[~/…/PicoCtf/Cryptography/codes/Sharesecret]
└─$ python3 code.py      
Shared secret: 896829247029805137379019231392423511831695744418274172381660663300487194077296709832921336918859919240152541104983503701113430020491393255108443422021810927595683086546513365492211610705251667499154870533633077647415643995507529101437594116973965271221235779046747884401625109540370541717335917683195778895705322466
Key byte: 226
Flag: picoCTF{dh_s3cr3t_32ec2679}
                                          
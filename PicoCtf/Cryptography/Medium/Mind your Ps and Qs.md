Problem : https://learn.cylabacademy.org/library/162

File path : PicoCtf/Cryptography/flagelemts/Mind your Ps and Qs

Soln :

St 0 : 

https://www.dcode.fr/rsa-cipher  go there put values of  3 select " Computed values (C,D,E,N,P,Q,…)"

================>>>

St-1

p	1891771437429478964908181306574287207137
q	501332739776173570344039681219489434626477
φ	94840695775683079968481817163954716578431324423373241003463893388115455340173273




before run code : 
python3 -m venv venv
source venv/bin/activate
pip install pycryptodome 

code : PicoCtf/Cryptography/flagelemts/Mind your Ps and Qs/rsaalgo.py
┌──(venv)─(samin㉿kali)-[~/…/PicoCtf/Cryptography/flagelemts/Mind your Ps and Qs]
└─$ python3 rsaalgo.py       

```python
b'\n}19ea7cd1_do0g_0n_N_11ams{FTCocip'

```

now go there : https://www.dcode.fr/reverse-writing

paste it found flag ==> 'picoCTF{sma11_N_n0_g0od_1dc7ae91}n\'b

```python
picoCTF{sma11_N_n0_g0od_1dc7ae91}
```


OR : 

After St0 Clicking ' Plaintext as Character string"  we found this " }19ea7cd1_do0g_0n_N_11ams{FTCocip"
then https://www.dcode.fr/reverse-writing go there  paste it ....and found flag => picoCTF{sma11_N_n0_g0od_1dc7ae91}   



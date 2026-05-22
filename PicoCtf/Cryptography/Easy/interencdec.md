
Problem : https://learn.cylabacademy.org/library/418 

file :  PicoCtf/Cryptography/flagelemts/enc_flag
Soln:


┌──(samin㉿kali)-[~]
└─$ echo "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgyeG9OakJzTURCcGZRPT0nCg==
" | base64 --decode

b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ=='
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~]
└─$ echo "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ==" | base64 --decode     

wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}  

then [Go there ](https://www.dcode.fr/caesar-cipher) 
paste wpjvJAM{jhlzhy_k3jy9wa3k_lh60l00i}   this Found flag : 

```python
picoCTF{caesar_d3cr9pt3d_ea60e00b}   
```
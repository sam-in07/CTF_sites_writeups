https://learn.cylabacademy.org/library/134
Best Stuff - Cheap Stuff, Buy Buy Buy...

PicoCtf/Reverse_eng/Medium/Files/shop/source

soln : 



Judging from the disassembly and the store selling the Fruitful Flag for more money than is in my wallet, I need to buy this item in order to obtain the flag, but I don’t have enough money.

A common vulnerability in these kinds of puzzles is tricking the software by buying or selling a negative number of items. I tried this theory out and it worked,

After playing around for a bit, I sold a negative number of item.... and ended up with a negative value for money. Through this I realized I should also be able to buy negative numbers of items since the shop probably only checks if there are less than how many items are in their stock. I bought a negative number of items and sure enough, ended up with a large enough sum of coins to buy a flag.

┌──(samin㉿kali)-[~]
└─$ nc wily-courier.picoctf.net 52185.
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
1
How many do you want to buy?
-30
You have 490 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      38
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 48 100 56 57 57 48 56 101 99 125 10]
                                                                                                                                                                                                                                           
┌──(samin㉿kali)-[~]
└─$ 

https://gchq.github.io/CyberChef/#recipe=From_Charcode('Space',10)

picoCTF{b4d_brogrammer_0d89908ec}
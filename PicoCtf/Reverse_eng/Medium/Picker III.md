https://learn.cylabacademy.org/library/402    
Can you figure out how this program works to get the flag?


PicoCtf/Reverse_eng/Medium/Files/patrikparker/2no/picker-III.py
Soln :


Picker III also tries to fix the issues of its predecessor. It locks down the user, for sure, but still leaves a gap that can be exploited. This vulnerability is mostly leveraged through “write_variable”.

The programmer has limited the functions we can call to a table of names. However, this table is just a variable and in the table is included a function called “write_variable”. We’ll actually use “read_variable” first, to get a string of the table. In the source code, the table is formatted specially by escaping the newline present at the end of each line. Calling read_variable will give us a string we can modify and give back to the program through write_variable. We must be careful to maintain the length of the string as given while still inserting our win function into the table. The check_table function makes sure that the length of the string is correct per the size of each entry and how many entries are expected. Be careful copying and pasting the result of read_variable as there are trailing spaces you want, but you don’t want to copy the newline of the line. Lastly, don’t forget to enclose your new table in quotes, so the text is interpreted as a string.



┌──(samin㉿kali)-[~/…/Medium/Files/patrikparker/2no]
└─$ nc saturn.picoctf.net 52873
==> ?

This program fixes vulnerabilities in its predecessor by limiting what
functions can be called to a table of predefined functions. This still puts
the user in charge, but prevents them from calling undesirable subroutines.

* Enter 'quit' to quit the program.
* Enter 'help' for this text.
* Enter 'reset' to reset the table.
* Enter '1' to execute the first function in the table.
* Enter '2' to execute the second function in the table.
* Enter '3' to execute the third function in the table.
* Enter '4' to execute the fourth function in the table.

Here's the current table:
  
1: print_table
2: read_variable
3: write_variable
4: getRandomNumber
==> 3
Please enter variable name to write: getRandomNumber
Please enter new value of variable: win
==> 2
Please enter variable name to read: getRandomNumber
<function win at 0x7a9087921dc0>
==> 4
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x37 0x68 0x31 0x35 0x5f 0x31 0x35 0x5f 0x77 0x68 0x34 0x37 0x5f 0x77 0x33 0x5f 0x67 0x33 0x37 0x5f 0x77 0x31 0x37 0x68 0x5f 0x75 0x35 0x33 0x72 0x35 0x5f 0x31 0x6e 0x5f 0x63 0x68 0x34 0x72 0x67 0x33 0x5f 0x32 0x32 0x36 0x64 0x64 0x32 0x38 0x35 0x7d 
==>                                                                                                                                   
┌──(samin㉿kali)-[~/…/Medium/Files/patrikparker/2no]
└─$ 

https://github.com/noamgariani11/picoGym-Exclusive-Writeup/blob/main/Reverse%20Engineering/Picker_III.md
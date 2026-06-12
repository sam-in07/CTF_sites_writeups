https://learn.cylabacademy.org/library/60

This vault uses for-loops and byte arrays.

The source code for this vault is here: VaultDoor3.java

PicoCtf/Reverse_eng/Medium/Files/voldoor/VaultDoor3.java


soln : 


```python
def checkPassword(password):
    if not len(password) == 32:
        return False
    buffer = [""] * 32

    for i in range(8):
        buffer[i] = password[i]

    for i in range(8, 16):
        buffer[i] = password[23 - i]
    
    for i in range(16, 32, 2):
        buffer[i] = password[46 - i]
    
    for i in range(31, 16, -2):
        buffer[i] = password[i]
    print(''.join(buffer))  # Combine and print the reconstructed password

checkPassword("jU5t_a_sna_3lpm15g64e_u_4_m1r74d")



```

Key Observations and Adjustments
Python For Loops vs. Java For Loops:
In Java, the condition i >= 17 allows the loop to include index 17. However, in Python, the range function excludes the endpoint. To replicate the behavior, I adjusted the range to go from 31 to 16 in steps of -2.
Index Calculations:
The values of 23 - i and 46 - i reverse the order of specific characters in the string. By carefully replicating these transformations, we can decode the original password.
Output:
The script outputs the reconstructed password, which is the flag.



jU5t_a_s1mpl3_an4gr4m_4_u_e1675d


picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e1675d}


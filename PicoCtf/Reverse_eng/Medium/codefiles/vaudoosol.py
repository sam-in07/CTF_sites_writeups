# Reconstruct flag based on check_password constraints

flag = [''] * 32  # create empty list of 32 characters

# Fill in characters according to check_password
flag[0]  = 'd'
flag[1]  = '3'
flag[2]  = '5'
flag[3]  = 'c'
flag[4]  = 'r'
flag[5]  = '4'
flag[6]  = 'm'
flag[7]  = 'b'
flag[8]  = 'l'
flag[9]  = '3'
flag[10] = '_'
flag[11] = 't'
flag[12] = 'H'
flag[13] = '3'
flag[14] = '_'
flag[15] = 'c'
flag[16] = 'H'
flag[17] = '4'
flag[18] = 'r'
flag[19] = '4'
flag[20] = 'c'
flag[21] = 'T'
flag[22] = '3'
flag[23] = 'r'
flag[24] = '5'
flag[25] = '_'
flag[26] = '7'
flag[27] = 'f'
flag[28] = 'f'
flag[29] = 'a'
flag[30] = '9'
flag[31] = '4'

# Combine into string
flagtext = ''.join(flag)

# Wrap in picoCTF{} as the code expects
full_flag = f"picoCTF{{{flagtext}}}"
print(full_flag)
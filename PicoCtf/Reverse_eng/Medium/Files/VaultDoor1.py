def check_password(password: str) -> bool:
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
            password[10] == '_' and
            password[5]  == '4' and
            password[9]  == '3' and
            password[11] == 't' and
            password[15] == 'c' and
            password[8]  == 'l' and
            password[12] == 'H' and
            password[20] == 'c' and
            password[14] == '_' and
            password[6]  == 'm' and
            password[24] == '5' and
            password[18] == 'r' and
            password[13] == '3' and
            password[19] == '4' and
            password[21] == 'T' and
            password[16] == 'H' and
            password[27] == 'f' and
            password[30] == '9' and
            password[25] == '_' and
            password[22] == '3' and
            password[28] == 'f' and
            password[26] == '7' and
            password[31] == '4')


def main():
    user_input = input("Enter vault password: ")
    input_str = user_input[len("picoCTF{"):-1]
    if check_password(input_str):
        print("Access granted.")
    else:
        print("Access denied!")


if __name__ == "__main__":
    main()
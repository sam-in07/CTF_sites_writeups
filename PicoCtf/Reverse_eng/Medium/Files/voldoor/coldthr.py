def check_password(password: str) -> bool:
    if len(password) != 32:
        return False
    buffer = [''] * 32
    i = 0
    while i < 8:
        buffer[i] = password[i]
        i += 1
    while i < 16:
        buffer[i] = password[23 - i]
        i += 1
    while i < 32:
        buffer[i] = password[46 - i]
        i += 2
    i = 31
    while i >= 17:
        buffer[i] = password[i]
        i -= 2
    s = ''.join(buffer)
    return s == "jU5t_a_sna_3lpm15g64e_u_4_m1r74d"


def main():
    user_input = input("Enter vault password: ")
    input_str = user_input[len("picoCTF{"):-1]
    if check_password(input_str):
        print("Access granted.")
    else:
        print("Access denied!")


if __name__ == "__main__":
    main()
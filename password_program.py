# Name: Andrew Goldstein

def encode(original_password):  # based on given password, encodes and returns an encoded password
    encoded_password = ""
    encoded_char_value = ""
    for i in original_password:
        if (int(i) + 3) > 10:
            encoded_char_value = str((int(i) + 3) % 10)
        else:
            encoded_char_value = str(int(i) + 3)

        encoded_password = encoded_password + encoded_char_value
    return encoded_password


def main():
    user_input = None
    password_to_encode = ""
    encoded_password = ""

    # prints menu, asks for user input and runs corresponding function or closes program
    while user_input != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = int(input("\nPlease enter an option: "))

        if user_input == 1:
            password_to_encode = input("Please enter your password to encode: ")
            encoded_password = encode(password_to_encode)
            print("Your password has been encoded and stored!\n")


if __name__ == "__main__":
    main()

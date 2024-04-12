
# Lab 9 - Jen is Encode

def encode(password):
    encoded = ""
    for each_char in password:
        each_char = int(each_char)
        each_char += 3
        encoded += str(each_char)

    return encoded
def decode(password):
    decoded = ""
    for each_char in password:
        each_char = int(each_char)
        each_char -= 3
        decoded += str(each_char)
    return decoded


menu = print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

choice = (input("Please enter an option: "))


while choice == "1" or choice == "2" or choice == "3":
    if choice == "2":
        y = (decode(x))
        print(f"The encoded password is {x}, and the original password is {y}")
        choice = (input("Please enter an option: "))
    elif choice == "1":
        password_enc = (input("Insert the password to encode: "))
        x = (encode(password_enc))
        print("Your password has been encoded and stored!")
        choice = (input("Please enter an option: "))
    elif choice == "3":
        break

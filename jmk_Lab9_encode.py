
# Lab 9 - Jen is Encode

def encode(password):
    encoded = ""
    for each_char in password:
        each_char = int(each_char)
        each_char += 3
        encoded += str(each_char)

    return encoded

def encode_password(input_password):
    encoded_password = ""
    for ch in input_password:
        encoded_password += chr(ord(ch) + 3)
    return encoded_password



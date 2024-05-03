def extend_key(key, length):
    extended_key = key
    while len(extended_key) < length:
        extended_key += key
    return extended_key[:length]

def encrypt(plain_text, key):
    key = extend_key(key, len(plain_text))
    encrypted_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            shift = ord(key[i].upper()) - 65
            if char.islower():
                encrypted_text += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                encrypted_text += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    key = extend_key(key, len(cipher_text))
    decrypted_text = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        if char.isalpha():
            shift = ord(key[i].upper()) - 65
            if char.islower():
                decrypted_text += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                decrypted_text += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plain_text = "Sheislistening"
key = "PASCAL"
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

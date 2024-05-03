def encrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - 97 + ord(key[key_index]) - 97) % 26) + 97)
            else:
                encrypted_char = chr(((ord(char) - 65 + ord(key[key_index]) - 97) % 26) + 65)
            encrypted_text += encrypted_char
            key_index += 1
            if key_index == len(key):
                key += encrypted_char.lower() if char.islower() else encrypted_char.upper()
                key_index = 0
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    decrypted_text = ""
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - 97 - (ord(key[key_index]) - 97)) % 26) + 97)
            else:
                decrypted_char = chr(((ord(char) - 65 - (ord(key[key_index]) - 97)) % 26) + 65)
            decrypted_text += decrypted_char
            key_index += 1
            if key_index == len(key):
                key += decrypted_char.lower() if char.islower() else decrypted_char.upper()
                key_index = 0
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plain_text = "Hello, World!"
key = "key"
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

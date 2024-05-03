def encrypt(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - key) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - 65 - key) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

plain_text = input("Enter the plain text: ")
key = int(input("Enter the key: "))
# plain_text = "Hello, World!"
# key = 3
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)

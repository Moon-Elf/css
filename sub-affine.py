def encrypt(plain_text, key_a, key_b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((ord(char) - 97) * key_a + key_b) % 26 + 97)
            else:
                encrypted_text += chr(((ord(char) - 65) * key_a + key_b) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def decrypt(cipher_text, key_a, key_b):
    decrypted_text = ""
    inverse_key_a = mod_inverse(key_a, 26)
    if inverse_key_a is None:
        return "Error: The key 'a' does not have a multiplicative inverse."
    
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(((ord(char) - 97 - key_b) * inverse_key_a) % 26 + 97)
            else:
                decrypted_text += chr(((ord(char) - 65 - key_b) * inverse_key_a) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plain_text = "hello"
key_a = 7
key_b = 2

encrypted_text = encrypt(plain_text, key_a, key_b)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key_a, key_b)
print("Decrypted text:", decrypted_text)

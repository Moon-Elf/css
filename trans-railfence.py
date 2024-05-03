def encrypt(plain_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plain_text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction = -direction

    cipher_text = ''.join(''.join(row) for row in fence)
    return cipher_text

def decrypt(cipher_text, rails):
    fence = [[''] * len(cipher_text) for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction = -direction

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*' and index < len(cipher_text):
                fence[i][j] = cipher_text[index]
                index += 1

    rail = 0
    direction = 1
    plain_text = ''
    for i in range(len(cipher_text)):
        plain_text += fence[rail][i]
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction = -direction

    return plain_text

# Example usage:
plain_text = "meetmeatthepark"
rails = 2
encrypted_text = encrypt(plain_text, rails)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, rails)
print("Decrypted text:", decrypted_text)

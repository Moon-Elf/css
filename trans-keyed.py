def keyed_transformation_encrypt(plain_text, key):
    if (len(plain_text) % len(str(key)) != 0):
        plain_text += "x"*(5 - (len(plain_text) // len(str(key))))
    arr =[]
    for i in range(0,len(plain_text),len(str(key))):
        arr.append([x for x in plain_text[i:i+ len(str(key))]])
    print(arr)
    cipher = ""
    
    for i in arr:
        print(i)
        for j in str(key):
            print(j)
            cipher += i[int(j)-1]
        cipher += " "
    return cipher

# Example usage:
plaintext = "enemyattacktonight"
key = 31452
encrypted_text = keyed_transformation_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
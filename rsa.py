import socket, math, os
public_key = None
private_key = None
n = None
def setkeys():
    global public_key, private_key, n
    prime1 = 61  # First prime number P
    prime2 = 53  # Second prime number Q
    n = prime1 * prime2
    tot_n = (prime1 - 1) * (prime2 - 1)
    e = 7
    while True:
        if math.gcd(e, tot_n) == 1:
            break
        e += 1
    public_key = e
    d = 2
    while True:
        if (d * e) % tot_n == 1:
            break
        d += 1
    private_key = d
def encrypt(message):
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text
def decrypt(encrypted_text):
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted
def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded
def decoder(encoded):
    s = ''
    for num in encoded:
        s += chr(decrypt(num))
    return s
def run_server():
    host = '192.168.0.102'
    port = 8080
    totalclient = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalclient)
    connections = []
    print('\nWaiting for User to connect...')
    conn, addr = sock.accept()
    connections.append((conn, addr))
    print('Connected with User at', addr)
    for conn, addr in connections:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('Public Key of Sender', addr, ':', data)
        response = input('Enter your Plain Text: ')
        encoded_response = encoder(response)
        print(f'Encrypted Message: {encoded_response}')
        print("Sending the Encrypted Message...")
        conn.send(','.join(str(p) for p in encoded_response).encode())
        conn.close()
    sock.close()
def run_client():
    host = '192.168.0.102'
    port = 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    message = input('Enter your Public Key: ')
    sock.sendall(message.encode())
    encoded_response = sock.recv(1024).decode().split(',')
    print('Received Encrypted Message: ', encoded_response)
    decoded_response = decoder([int(num) for num in encoded_response])
    print('Decrypted Text: ', decoded_response)
    sock.close()
def design():
    os.system('cls')
    print("\t\t\t\t__________________________________\n")
    print("\t\t\t\tRSA Encryption/Decryption Program")
    print("\t\t\t\t__________________________________")
if __name__ == '__main__':
    setkeys()
    design()
    choice = input("\nOptions:\n\t'e' for Encrypt\n\t'd' for Decrypt\n\n\tChoice: ")
    if choice.lower() == 'e':
        run_server()
    elif choice.lower() == 'd':
        run_client()
    else:
        print("Invalid choice.")

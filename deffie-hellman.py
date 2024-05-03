import socket, random, os

def generate_key(p, g, private_key):
    return (g ** private_key) % p

def send_public_key(connection, public_key):
    connection.send(str(public_key).encode())

def receive_public_key(connection):
    return int(connection.recv(1024).decode())

def calculate_shared_secret(public_key, private_key, p):
    return (public_key ** private_key) % p

def sender():
    # Commonly agreed prime modulus and generator
    p = 23
    g = 5

    # Sender's private key
    sender_private_key = random.randint(1, 10)

    # Establish connection
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_socket.bind(('localhost', 12345))
    sender_socket.listen(1)
    print("Waiting for connection...")
    connection, address = sender_socket.accept()
    print("Connected to:", address)

    # Generate and send public key
    sender_public_key = generate_key(p, g, sender_private_key)
    send_public_key(connection, sender_public_key)

    # Receive receiver's public key
    receiver_public_key = receive_public_key(connection)

    # Calculate shared secret
    shared_secret = calculate_shared_secret(receiver_public_key, sender_private_key, p)
    print("Shared secret:", shared_secret)

    # Close connection
    connection.close()
    sender_socket.close()

def receiver():
    # Commonly agreed prime modulus and generator
    p = 23
    g = 5

    # Receiver's private key
    receiver_private_key = random.randint(1, 10)

    # Establish connection
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.connect(('localhost', 12345))
    print("Connected to sender...")

    # Receive sender's public key
    sender_public_key = receive_public_key(receiver_socket)

    # Generate and send public key
    receiver_public_key = generate_key(p, g, receiver_private_key)
    send_public_key(receiver_socket, receiver_public_key)

    # Calculate shared secret
    shared_secret = calculate_shared_secret(sender_public_key, receiver_private_key, p)
    print("Shared secret:", shared_secret)

    # Close connection
    receiver_socket.close()

def design():
    os.system('cls')
    print("\t\t\t\t__________________________________\n")
    print("\t\t\t\t    Deffie Hellman Key Exchange")
    print("\t\t\t\t__________________________________")

if __name__ == "__main__":
    design()
    print("Options:\n1. Sender\n2. Receiver\n")
    choice = int(input("Enter choice: "))
    if choice == 1:
        sender()
    elif choice == 2:
        receiver()
    else:
        print("Invalid choice.")

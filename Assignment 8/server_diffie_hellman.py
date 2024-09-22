import socket
import random


def generate_private_key(p):
    """Generate a private key."""
    return random.randint(2, p-2)


def calculate_public_key(g, private_key, p):
    """Calculate the public key."""
    return pow(g, private_key, p)


def calculate_shared_secret(public_key, private_key, p):
    """Calculate the shared secret."""
    return pow(public_key, private_key, p)


def start_server(host='localhost', port=5000):
    # p = 23
    # g = 5
    p = 104729  # Shared prime number --> 104729 (which is the 10000th prime number)
    g = 2   # Shared base --> Primitive Root g: 2

    # Generate server's private and public keys
    private_key = generate_private_key(p)
    public_key = calculate_public_key(g, private_key, p)

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started. Listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"\nConnected by {addr}")

    # Send the server's public key to the client
    conn.sendall(str(public_key).encode())

    # Receive the client's public key
    client_public_key = int(conn.recv(1024).decode())
    print(f"\nReceived Client's Public Key: {client_public_key}")

    # Calculate the shared secret
    shared_secret = calculate_shared_secret(client_public_key, private_key, p)
    print(f"\nShared Secret (Server): {shared_secret}")

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()

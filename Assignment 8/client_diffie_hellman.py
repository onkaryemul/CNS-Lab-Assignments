import socket
import random

def generate_private_key(p):
    """Generate a private key."""
    private_key = random.randint(2, p - 2)
    print(f"\nGenerated Private Key: {private_key}")
    return private_key

def calculate_public_key(g, private_key, p):
    """Calculate the public key."""
    public_key = pow(g, private_key, p)
    print(f"\nCalculated Public Key: {public_key}")
    return public_key

def calculate_shared_secret(public_key, private_key, p):
    """Calculate the shared secret."""
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

def start_client(server_host='localhost', server_port=5000):
    # Take p and g as user input
    p = int(input("\nEnter a prime number (p): "))
    g = int(input("\nEnter a primitive root (g): "))

    # Generate client's private and public keys
    private_key = generate_private_key(p)
    public_key = calculate_public_key(g, private_key, p)

    # Create client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Receive the server's public key
    server_public_key = int(client_socket.recv(1024).decode())
    print(f"\nReceived Server's Public Key: {server_public_key}")

    # Send the client's public key to the server
    client_socket.sendall(str(public_key).encode())

    # Calculate the shared secret
    shared_secret = calculate_shared_secret(server_public_key, private_key, p)
    print(f"\nShared Secret (Client): {shared_secret}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

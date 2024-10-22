import socket
import random

def generate_private_key(p):
    """Generate a private key."""
    private_key = random.randint(2, p - 2)
    print(f"\nGenerated Server's Private Key: {private_key}")
    return private_key

def calculate_public_key(g, private_key, p):
    """Calculate the public key."""
    public_key = pow(g, private_key, p)
    print(f"\nCalculated Server's Public Key: {public_key}")
    return public_key

def calculate_shared_secret(public_key, private_key, p):
    """Calculate the shared secret."""
    shared_secret = pow(public_key, private_key, p)
    return shared_secret

def start_server(host='localhost', port=5000):
    # Take p and g as user input
    p = int(input("\nEnter a prime number (p): "))
    g = int(input("\nEnter a primitive root (g): "))

    # Generate server's private and public keys
    private_key = generate_private_key(p)
    public_key = calculate_public_key(g, private_key, p)

    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"\nServer started. Listening on {host}:{port}")

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

# For 
# p: 1014273607262027361
# For 
# g: 2

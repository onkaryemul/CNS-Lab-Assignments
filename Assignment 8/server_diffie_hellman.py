import socket
import random
from sympy import isprime, primerange

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

def find_next_prime(n):
    """Find the next prime number greater than or equal to n."""
    if isprime(n):
        return n
    else:
        for prime in primerange(n + 1, n * 2):
            return prime

def find_primitive_roots(p, count=5):
    """Find the first `count` primitive roots of prime `p`."""
    roots = []
    for g in range(2, p):
        seen = set(pow(g, power, p) for power in range(1, p))
        if len(seen) == p - 1:
            roots.append(g)
        if len(roots) >= count:
            break
    return roots

def start_server(host='localhost', port=5000):
    # Create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"\nServer started. Listening on {host}:{port}")

    # Take p as user input and validate it
    p = int(input("\nEnter a prime number (p): "))
    p = find_next_prime(p)
    print(f"\nValidated Prime Number (p): {p}")

    # Find and list primitive roots of p
    primitive_roots = find_primitive_roots(p)
    print(f"\nFirst Five Primitive Roots for {p}: {primitive_roots}")

    # Take g as user input and validate it
    g = int(input(f"\nChoose a primitive root (g) from the above list: "))
    while g not in primitive_roots:
        print("Invalid choice. Please choose a primitive root from the list.")
        g = int(input(f"\nChoose a primitive root (g) from the above list: "))

    # Generate server's private and public keys
    private_key = generate_private_key(p)
    public_key = calculate_public_key(g, private_key, p)

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

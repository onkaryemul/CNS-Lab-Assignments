import random
from sympy import isprime, mod_inverse

def generate_prime_candidate(length):
    """Generate an odd integer randomly."""
    p = random.getrandbits(length)
    # Ensure p is odd
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length):
    """Generate a prime number."""
    p = 4
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p


def generate_keypair(keysize):
    """Generate RSA public and private keys."""
    # Generate two large primes p and q
    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)

    print("\np: ", p)
    print("\nq: ", q)
    
    # Compute n = p * q
    n = p * q
    
    # Compute Euler's Totient φ(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)
    
    # Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)
    
    # Compute d, the modular inverse of e
    d = mod_inverse(e, phi)
    
    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n))


def gcd(a, b):
    """Compute the greatest common divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a


def encrypt(public_key, plaintext):
    """Encrypt plaintext using the public key."""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher


def decrypt(private_key, ciphertext):
    """Decrypt ciphertext using the private key."""
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)


def main():
    """Run RSA algorithm."""
    print("RSA Encryption/Decryption")
    
    keysize = 2048  # Keysize in bits
    
    # Generate public and private keys
    public_key, private_key = generate_keypair(keysize)
    
    print(f"\nPublic key: {public_key}")
    print(f"Private key: {private_key}")
    
    # Input plaintext
    plaintext = input("\nEnter a message to encrypt: ")
    
    # Encrypt the message
    encrypted_msg = encrypt(public_key, plaintext)
    print(f"\nEncrypted message: {encrypted_msg}")
    
    # Decrypt the message
    decrypted_msg = decrypt(private_key, encrypted_msg)
    print(f"\nDecrypted message: {decrypted_msg}")


if __name__ == "__main__":
    main()

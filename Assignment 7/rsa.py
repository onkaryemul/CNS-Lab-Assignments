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

def gcd(a, b):
    """Compute the greatest common divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def generate_keypair(keysize):
    """Generate RSA public and private keys."""
    # Generate two large primes p and q
    p = generate_prime_number(keysize)
    q = generate_prime_number(keysize)

    print("\np (prime):", p)
    print("q (prime):", q)
    
    # Compute n = p * q
    n = p * q
    print("n (p * q):", n)
    
    # Compute Euler's Totient φ(n) = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)
    print("phi (Euler's Totient):", phi)
    
    # Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)
    print("e (public exponent):", e)
    
    # Compute d, the modular inverse of e
    d = mod_inverse(e, phi)
    print("d (private exponent):", d)
    
    # Public key (e, n) and Private key (d, n)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypt plaintext using the public key."""
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    print("\nIntermediate Encryption Steps:")
    for i, char in enumerate(plaintext):
        print(f"Character '{char}' -> Cipher Value: {cipher[i]}")
    return cipher

def decrypt(private_key, ciphertext):
    """Decrypt ciphertext using the private key."""
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    print("\nIntermediate Decryption Steps:")
    for i, val in enumerate(ciphertext):
        print(f"Cipher Value {val} -> Character: {plain[i]}")
    return ''.join(plain)

def main():
    """Run RSA algorithm with menu-driven interface."""
    public_key, private_key = None, None
    while True:
        print("\nMenu:")
        print("1. Generate Key Pair")
        print("2. Encrypt a Message")
        print("3. Decrypt a Message")
        print("4. Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            keysize = int(input("Enter key size (e.g., 1024, 2048): "))
            public_key, private_key = generate_keypair(keysize)
            print(f"\nPublic key: {public_key}")
            print(f"Private key: {private_key}")
        
        elif choice == '2':
            if not public_key:
                print("Please generate keys first (Option 1).")
                continue
            plaintext = input("Enter a message to encrypt: ")
            encrypted_msg = encrypt(public_key, plaintext)
            print(f"\nEncrypted Message: {encrypted_msg}")
        
        elif choice == '3':
            if not private_key:
                print("Please generate keys first (Option 1).")
                continue
            encrypted_msg = input("Enter the encrypted message (as a list of integers): ")
            try:
                encrypted_msg = list(map(int, encrypted_msg.strip('[]').split(',')))
            except ValueError:
                print("Invalid input. Please enter integers separated by commas.")
                continue
            decrypted_msg = decrypt(private_key, encrypted_msg)
            print(f"\nDecrypted Message: {decrypted_msg}")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()


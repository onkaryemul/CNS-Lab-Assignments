import hashlib


def calculate_sha1(text):
    # Create a new SHA-1 hash object
    sha1_hash = hashlib.sha1()
    
    # Encode the input text to bytes and update the hash object
    sha1_hash.update(text.encode('utf-8'))
    
    # Get the hexadecimal representation of the digest
    digest = sha1_hash.hexdigest()
    
    return digest


if __name__ == "__main__":
    # Input text
    text = input("Enter the text to calculate SHA-1 hash: ")
    
    # Calculate SHA-1 message digest
    sha1_digest = calculate_sha1(text)
    
    # Output the result
    print(f"SHA-1 Digest: {sha1_digest}")


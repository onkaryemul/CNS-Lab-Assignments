from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(plain_text, key):
    """
    Encrypt the plain text using DES algorithm.
    
    Parameters:
    plain_text (str): The text to be encrypted.
    key (bytes): The encryption key (must be 8 bytes long).
    
    Returns:
    bytes: The encrypted cipher text.
    """
    print(f"\n[Encryption Process]")
    print(f"Plain Text: {plain_text}")
    
    # Initialize the DES cipher in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)
    print(f"DES Cipher initialized with ECB mode and key: {key.hex()}")
    
    # Padding the plain text to match DES block size (8 bytes)
    padded_text = pad(plain_text.encode(), DES.block_size)
    print(f"Padded Plain Text (in hexadecimal): {padded_text.hex()}")
    
    # Encrypting the padded text
    encrypted_text = cipher.encrypt(padded_text)
    print(f"Encrypted Text (in hexadecimal): {encrypted_text.hex()}")
    
    return encrypted_text

def des_decrypt(cipher_text, key):
    """
    Decrypt the cipher text using DES algorithm.
    
    Parameters:
    cipher_text (bytes): The encrypted text to be decrypted.
    key (bytes): The decryption key (must be 8 bytes long).
    
    Returns:
    str: The decrypted plain text.
    """
    print(f"\n[Decryption Process]")
    print(f"Cipher Text to Decrypt (in hexadecimal): {cipher_text.hex()}")
    
    # Initialize the DES cipher in ECB mode for decryption
    cipher = DES.new(key, DES.MODE_ECB)
    print(f"DES Cipher initialized with ECB mode and key: {key.hex()}")
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(cipher_text)
    print(f"Decrypted Padded Text (in hexadecimal): {decrypted_padded_text.hex()}")
    
    # Unpad the decrypted text
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    print(f"Decrypted Text (unpadded): {decrypted_text.decode()}")
    
    return decrypted_text.decode()

def main():
    """
    The main function to run the DES encryption and decryption program.
    """
    # Generate a random 8-byte key for DES
    key = get_random_bytes(8)
    print(f"\nGenerated Key (in hexadecimal): {key.hex()}")

    while True:
        print("\nMenu:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Quit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            # Encrypt a message
            plain_text = input("\nEnter the plain text to encrypt: ")
            encrypted_text = des_encrypt(plain_text, key)
            print(f"\nFinal Encrypted Text (in hexadecimal): {encrypted_text.hex()}")
        
        elif choice == '2':
            # Decrypt a message
            encrypted_text_hex = input("\nEnter the Encrypted Text in hexadecimal to decrypt: ")
            encrypted_text = bytes.fromhex(encrypted_text_hex)
            
            # Decrypt the ciphertext
            try:
                decrypted_text = des_decrypt(encrypted_text, key)
                print(f"\nFinal Decrypted Text: {decrypted_text}")
            except ValueError as e:
                print(f"\nError during decryption: {e}")
        
        elif choice == '3':
            print("\nExiting the program.")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

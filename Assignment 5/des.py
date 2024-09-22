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
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = cipher.encrypt(padded_text)
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
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return decrypted_text.decode()


def main():
    """
    The main function to run the program.
    """
    print("\nDES Encryption and Decryption")
    
    # Generate a random 8-byte key for DES
    key = get_random_bytes(8)
    print(f"\nGenerated Key (in hexadecimal): {key.hex()}")
    
    # Input plaintext
    plain_text = input("Enter the plain text to encrypt: ")
    
    # Encrypt the plaintext
    encrypted_text = des_encrypt(plain_text, key)
    print(f"\nEncrypted Text (in hexadecimal): {encrypted_text.hex()}")
    
    # Decrypt the ciphertext
    decrypted_text = des_decrypt(encrypted_text, key)
    print(f"\nDecrypted Text: {decrypted_text}")


if __name__ == "__main__":
    main()

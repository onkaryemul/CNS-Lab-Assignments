from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
import hashlib


# Function to generate RSA private and public keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    
    return private_key, public_key


# Function to sign a message and print its hash
def sign_message(private_key, message):
    # Hash the message using SHA-256
    message_hash = hashlib.sha256(message.encode()).hexdigest()
    
    # Sign the hashed message using RSA private key
    signature = private_key.sign(
        bytes.fromhex(message_hash),  # Convert the hex hash to bytes
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    print(f"Hash of the message: {message_hash}")  # Print the message hash
    return signature, message_hash


# Function to verify the signature using the provided hash
def verify_signature(public_key, message_hash, signature):
    try:
        # Verify the signature using RSA public key
        public_key.verify(
            signature,
            bytes.fromhex(message_hash),  # Convert the hex hash back to bytes
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False


# Function to save keys to files
def save_keys_to_file(private_key, public_key):
    # Save private key
    with open("private_key.pem", "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
    # Save public key
    with open("public_key.pem", "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
    print("Keys saved to files: private_key.pem and public_key.pem")


# Menu for the digital signature system
def menu():
    private_key, public_key = None, None
    signature = None
    message_hash = None

    while True:
        print("\n===== Digital Signature System =====")
        print("1. Generate RSA Keys")
        print("2. Sign a Message")
        print("3. Verify Signature")
        print("4. Save Keys to Files")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # Generate RSA private and public keys
            private_key, public_key = generate_keys()
            print("\nRSA Keys Generated!")
        
        elif choice == '2':
            # Sign a message
            if private_key is None:
                print("You need to generate RSA keys first.")
            else:
                message = input("Enter the message to sign: ")
                signature, message_hash = sign_message(private_key, message)
                print("\nMessage signed successfully!")

        elif choice == '3':
            # Verify the signature
            if public_key is None or message_hash is None or signature is None:
                print("You need to sign a message first.")
            else:
                input_hash = input("Enter the hash of the message to verify: ")
                verification_result = verify_signature(public_key, input_hash, signature)
                if verification_result:
                    print("\nSignature verified successfully! The message is authentic.")
                else:
                    print("\nSignature verification failed! The message is not authentic.")

        elif choice == '4':
            # Save RSA keys to files
            if private_key is None or public_key is None:
                print("You need to generate RSA keys first.")
            else:
                save_keys_to_file(private_key, public_key)

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

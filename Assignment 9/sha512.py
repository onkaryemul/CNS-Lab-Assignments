import hashlib

# Function to hash a message using SHA-512
def sha512_encrypt(message):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(message.encode('utf-8'))  # Convert the message to bytes
    return sha512_hash.hexdigest()

# Function to verify the hash (like a decryption process)
def verify_hash(original_message, provided_hash):
    original_hash = sha512_encrypt(original_message)
    return original_hash == provided_hash

# Menu-driven system
def menu():
    while True:
        print("\n===== SHA-512 Hashing System =====")
        print("1. Encrypt a message using SHA-512")
        print("2. Verify a message against a given hash")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to hash: ")
            hashed_message = sha512_encrypt(message)
            print(f"\nSHA-512 Hash: {hashed_message}")

        elif choice == '2':
            original_message = input("Enter the original message: ")
            provided_hash = input("Enter the hash to verify against: ")
            
            if verify_hash(original_message, provided_hash):
                print("\nVerification successful! The message matches the provided hash.")
            else:
                print("\nVerification failed! The message does not match the provided hash.")

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    menu()



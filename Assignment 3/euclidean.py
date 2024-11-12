def euclidean_algorithm(a, b):
    """
    Compute the GCD of a and b using the Euclidean algorithm.
    
    Parameters:
    a (int): First integer.
    b (int): Second integer.
    
    Returns:
    int: The GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def extended_euclidean_algorithm(a, b):
    """
    Compute the GCD of a and b, as well as the coefficients x and y 
    such that ax + by = gcd(a, b) using the Extended Euclidean algorithm.
    
    Parameters:
    a (int): First integer.
    b (int): Second integer.
    
    Returns:
    tuple: (gcd, x, y) where gcd is the GCD of a and b, and x, y are 
    the coefficients of Bézout's identity.
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


def modular_inverse(x, z):
    """
    Find the modular inverse of x mod z using the Extended Euclidean algorithm.
    
    Parameters:
    x (int): The integer whose modular inverse is to be found.
    z (int): The modulus.
    
    Returns:
    int: The modular inverse of x mod z if it exists, otherwise None.
    """
    gcd, inv, _ = extended_euclidean_algorithm(x, z)
    if gcd != 1:
        # Inverse does not exist if gcd(x, z) != 1
        return None
    else:
        # Make sure the inverse is positive
        return inv % z


def main():
    """
    The main function to run the program.
    """
    while True:
        print("\nEuclidean and Extended Euclidean Algorithm")
        print("1. Compute GCD using Euclidean Algorithm")
        print("2. Compute GCD and coefficients using Extended Euclidean Algorithm")
        print("3. Find Modular Inverse")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            a = int(input("\nEnter the first integer (a): "))
            b = int(input("Enter the second integer (b): "))
            gcd = euclidean_algorithm(a, b)
            print(f"\nGCD of {a} and {b} is: {gcd}")
        elif choice == '2':
            a = int(input("\nEnter the first integer (a): "))
            b = int(input("Enter the second integer (b): "))
            gcd, x, y = extended_euclidean_algorithm(a, b)
            print(f"\nGCD of {a} and {b} is: {gcd}")
            print(f"Coefficients x and y are: x = {x}, y = {y}")
            print(f"\nBézout's identity: {a}*({x}) + {b}*({y}) = {gcd}")
        elif choice == '3':
            x = int(input("\nEnter the integer (x) to find its modular inverse: "))
            z = int(input("Enter the modulus (z): "))
            inverse = modular_inverse(x, z)
            if inverse is None:
                print(f"\nNo modular inverse exists for {x} mod {z} (since gcd({x}, {z}) ≠ 1).")
            else:
                print(f"\nThe modular inverse of {x} mod {z} is: {inverse}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

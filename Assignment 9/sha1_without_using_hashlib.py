import struct

# Helper functions for bitwise operations
def left_rotate(n, b):
    """Left rotate a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def sha1_padding(message):
    """Pad the message to ensure the length is a multiple of 512 bits."""
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    # Padding with a '1' bit followed by '0's, and add the original message length in bits at the end
    message += b'\x80'  # append the bit '1' (10000000 in binary)
    
    # Pad with 0s so that the message length is 64 bits short of a multiple of 512
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    
    # Append the length of the original message in bits (64-bit big-endian integer)
    message += struct.pack('>Q', original_bit_len)
    
    return message


def sha1(message):
    """Calculate the SHA-1 hash of a message."""
    # Initial hash values (first 32 bits of the fractional parts of the square roots of the first 5 primes)
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Preprocessing: padding the message
    message = sha1_padding(message)

    # Process the message in successive 512-bit chunks (64 bytes each)
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        
        # Break chunk into sixteen 32-bit big-endian words
        w = [0] * 80
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j*4:(j*4)+4])[0]
        
        # Extend the sixteen 32-bit words into eighty 32-bit words
        for j in range(16, 80):
            w[j] = left_rotate((w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16]), 1)

        # Initialize hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to the result so far
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Produce the final hash value (big-endian)
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)


if __name__ == "__main__":
    # Input text
    text = input("Enter the text to calculate SHA-1 hash: ")

    # Convert the text to bytes and compute SHA-1 hash
    sha1_digest = sha1(text.encode('utf-8'))

    # Output the SHA-1 hash
    print(f"SHA-1 Digest: {sha1_digest}")


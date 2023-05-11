import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1,
            u2 - q * v2,
            u3 - q * v3,
            v1,
            v2,
            v3,
        )

    return u1 % m

def generate_keypair(p, q):
    # Calculate n = p * q
    n = p * q

    # Calculate the totient of n, phi(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # Find e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Calculate the modular inverse of e modulo phi
    d = mod_inverse(e, phi)

    # Return the public and private keys
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key

def rsa_encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def rsa_decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Example usage:
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

public_key, private_key = generate_keypair(p, q)
print("Public key:", public_key)
print("Private key:", private_key)

message = input("Enter a message to encrypt: ")

encrypted_message = rsa_encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = rsa_decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)

import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    e, n = pk
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    d, n = pk
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)


# Ask the user for two prime numbers
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

# Generate the public and private keys
public_key, private_key = generate_keypair(p, q)
print("Public key:", public_key)
print("Private key:", private_key)

# Ask the user for a message to encrypt
message = input("Enter a message to encrypt: ")

# Encrypt the message using the public key
ciphertext = encrypt(public_key, message)
print("Encrypted message:", ciphertext)

# Decrypt the message using the private key
plaintext = decrypt(private_key, ciphertext)
print("Decrypted message:", plaintext)

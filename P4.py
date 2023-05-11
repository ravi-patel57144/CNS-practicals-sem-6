import numpy as np

# Function to convert plaintext to matrix
def text_to_matrix(text, key_length):
    text = text.upper().replace(' ', '')
    matrix = []
    row = []
    for char in text:
        row.append(ord(char) - ord('A'))
        if len(row) == key_length:
            matrix.append(row)
            row = []
    if len(row) > 0:
        while len(row) < key_length:
            row.append(0)
        matrix.append(row)
    return np.array(matrix)

# Function to convert matrix to ciphertext
def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for num in row:
            text += chr(num % 26 + ord('A'))
    return text

# Function to calculate the multiplicative inverse of a number modulo 26
def multiplicative_inverse(num):
    for i in range(26):
        if (num * i) % 26 == 1:
            return i
    return -1

# Function to encrypt plaintext using Hill cipher
def hill_cipher_encrypt(plaintext, key):
    key_length = int(np.sqrt(len(key)))
    plaintext_matrix = text_to_matrix(plaintext, key_length)
    key_matrix = np.array(key).reshape(key_length, key_length)
    cipher_matrix = np.matmul(plaintext_matrix, key_matrix) % 26
    ciphertext = matrix_to_text(cipher_matrix)
    return ciphertext

# Function to decrypt ciphertext using Hill cipher
def hill_cipher_decrypt(ciphertext, key):
    key_length = int(np.sqrt(len(key)))
    ciphertext_matrix = text_to_matrix(ciphertext, key_length)
    key_matrix = np.array(key).reshape(key_length, key_length)
    det = int(round(np.linalg.det(key_matrix))) % 26

    # Check if the determinant is relatively prime to 26
    if np.gcd(det, 26) != 1:
        return "Invalid key. Cannot find multiplicative inverse."

    inv_key_matrix = np.linalg.inv(key_matrix)
    mul_inv = multiplicative_inverse(det)
    adj_matrix = (inv_key_matrix * det) % 26
    adj_matrix = (adj_matrix * mul_inv) % 26
    plaintext_matrix = np.matmul(ciphertext_matrix, adj_matrix) % 26
    plaintext = matrix_to_text(plaintext_matrix)
    return plaintext

# Get plaintext from user
plaintext = input("Enter the plaintext: ")

# Get key from user
key_str = input("Enter the key as a list of integers (e.g., 6 24 1 13): ")
key = [int(x) for x in key_str.split()]

# Check if key is square and its length matches plaintext
key_length = int(np.sqrt(len(key)))
if key_length * key_length != len(key):
    print("Invalid key length. It should be a perfect square.")
    exit(1)

# Encrypt the plaintext
ciphertext = hill_cipher_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = hill_cipher_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
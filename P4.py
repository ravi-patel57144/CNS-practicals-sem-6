import numpy as np

# Function to generate the key matrix from a given key string
def generate_key_matrix(key):
    # Convert the key to uppercase and remove any spaces
    key = key.upper().replace(" ", "")
    # Determine the size of the key matrix
    n = int(np.ceil(np.sqrt(len(key))))
    # Add padding to the key if necessary
    padding = n ** 2 - len(key)
    key += "X" * padding
    # Reshape the key into a square matrix
    key_matrix = np.array(list(key)).reshape(n, n)
    # Map the letters to numbers (A=0, B=1, etc.)
    key_matrix = np.array([[ord(c) - 65 for c in row] for row in key_matrix])
    return key_matrix


# Function to encrypt or decrypt plaintext using a key matrix
def hill_cipher(plaintext, key_matrix, mode):
    # Map the plaintext to numbers (A=0, B=1, etc.)
    plaintext = plaintext.upper().replace(" ", "")
    plaintext = np.array([ord(c) - 65 for c in plaintext])
    # Determine the size of the key matrix
    n = key_matrix.shape[0]
    # Add padding to the plaintext if necessary
    padding = n - len(plaintext) % n
    plaintext = np.append(plaintext, np.zeros(padding, dtype=int))
    # Reshape the plaintext into a matrix
    plaintext_matrix = plaintext.reshape(-1, n)
    # Encrypt or decrypt the plaintext matrix using the key matrix
    if mode == "encrypt":
        result_matrix = plaintext_matrix @ key_matrix % 26
    elif mode == "decrypt":
        # Find the determinant of the key matrix
        determinant = int(round(np.linalg.det(key_matrix)))
        # Check if the determinant is invertible (i.e., not divisible by 26)
        if determinant % 26 == 0:
            return "Error: Key matrix is not invertible"
        # Find the inverse of the key matrix
        inverse_determinant = [i for i in range(26) if (i * determinant) % 26 == 1][0]
        inverse_matrix = np.round((np.linalg.inv(key_matrix) * determinant * inverse_determinant) % 26).astype(int)
        # Decrypt the plaintext using the inverse key matrix
        result_matrix = plaintext_matrix @ inverse_matrix % 26
    # Map the resulting numbers back to letters (A=0, B=1, etc.)
    result = "".join([chr(c + 65) for row in result_matrix for c in row])
    return result


# Ask the user for plaintext and key
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

# Generate the key matrix
key_matrix = generate_key_matrix(key)

# Encrypt the plaintext with the key matrix
ciphertext = hill_cipher(plaintext, key_matrix, "encrypt")
print("Encrypted ciphertext:", ciphertext)

# Decrypt the ciphertext with the key matrix
decrypted = hill_cipher(ciphertext, key_matrix, "decrypt")
print("Decrypted plaintext:", decrypted)

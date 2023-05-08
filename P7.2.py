def transposition_encrypt(plaintext, key):
    # Pad the plaintext to be a multiple of the key length
    padding = (key - len(plaintext) % key) % key
    plaintext += ' ' * padding

    # Create the rows of the transposition matrix
    rows = [plaintext[i:i+key] for i in range(0, len(plaintext), key)]

    # Create the columns of the transposition matrix
    columns = ['' for i in range(key)]
    for i in range(key):
        for row in rows:
            columns[i] += row[i]

    # Join the columns together to create the ciphertext
    ciphertext = ''.join(columns)

    return ciphertext

def transposition_decrypt(ciphertext, key):
    # Calculate the number of rows needed for the transposition matrix
    rows = len(ciphertext) // key

    # Create the columns of the transposition matrix
    columns = [ciphertext[i::rows] for i in range(rows)]

    # Join the rows together to create the plaintext
    plaintext = ''.join(columns)

    return plaintext.rstrip()

# Ask the user for a message to encrypt and a key
plaintext = input("Enter a message to encrypt: ")
key = int(input("Enter a key: "))

# Encrypt the message using the Transposition cipher
ciphertext = transposition_encrypt(plaintext, key)
print("Encrypted message:", ciphertext)

# Decrypt the message using the Transposition cipher
decrypted_plaintext = transposition_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_plaintext)

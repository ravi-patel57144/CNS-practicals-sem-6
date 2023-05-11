def prepare_input(text):
    # Remove any non-alphabetic characters and convert to uppercase
    text = ''.join(filter(str.isalpha, text.upper()))
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    return text

def generate_playfair_key(keyword):
    # Create the Playfair key matrix
    keyword = prepare_input(keyword)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = keyword + alphabet
    key = ''.join(dict.fromkeys(key))
    return key

def generate_playfair_matrix(key):
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(key[i * 5 + j])
        matrix.append(row)
    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    plaintext = prepare_input(plaintext)
    matrix = generate_playfair_matrix(key)

    # Pad the plaintext with 'X' if the length is odd
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    encrypted_text = ""
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]

        i += 2

    return encrypted_text

def playfair_decrypt(encrypted_text, key):
    matrix = generate_playfair_matrix(key)

    decrypted_text = ""
    i = 0
    while i < len(encrypted_text):
        char1 = encrypted_text[i]
        char2 = encrypted_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]

        i += 2

    return decrypted_text

# Example usage:
plaintext = input("Enter Plaintext:")
keyword = input("Enter key:")

key = generate_playfair_key(keyword)

encrypted_text = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)

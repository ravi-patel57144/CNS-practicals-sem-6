def rail_fence_encrypt(plaintext, key):
    # Create the fence with empty cells
    fence = [['\n' for i in range(len(plaintext))] for j in range(key)]

    # Fill the fence with the plaintext
    direction = -1
    row, col = 0, 0
    for char in plaintext:
        # Reverse the direction if the fence edge is reached
        if row == 0 or row == key - 1:
            direction = -direction

        # Fill the fence with the plaintext character
        fence[row][col] = char
        col += 1
        row += direction

    # Collect the fence characters into the ciphertext
    ciphertext = []
    for i in range(key):
        for j in range(len(plaintext)):
            if fence[i][j] != '\n':
                ciphertext.append(fence[i][j])

    return ''.join(ciphertext)

def rail_fence_decrypt(ciphertext, key):
    # Create the fence with empty cells
    fence = [['\n' for i in range(len(ciphertext))] for j in range(key)]

    # Calculate the fence pattern
    direction = -1
    row, col = 0, 0
    for i in range(len(ciphertext)):
        # Reverse the direction if the fence edge is reached
        if row == 0 or row == key - 1:
            direction = -direction

        # Fill the fence with placeholder characters
        fence[row][col] = '*'
        col += 1
        row += direction

    # Fill the fence with the ciphertext characters
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*' and index < len(ciphertext):
                fence[i][j] = ciphertext[index]
                index += 1

    # Collect the fence characters into the plaintext
    plaintext = []
    direction = -1
    row, col = 0, 0
    for i in range(len(ciphertext)):
        # Reverse the direction if the fence edge is reached
        if row == 0 or row == key - 1:
            direction = -direction

        # Collect the plaintext character from the fence
        if fence[row][col] != '*':
            plaintext.append(fence[row][col])
            col += 1
        row += direction

    return ''.join(plaintext)

# Ask the user for a message to encrypt and a key
plaintext = input("Enter a message to encrypt: ")
key = int(input("Enter a key: "))

# Encrypt the message using the Rail Fence cipher
ciphertext = rail_fence_encrypt(plaintext, key)
print("Encrypted message:", ciphertext)

# Decrypt the message using the Rail Fence cipher
decrypted_plaintext = rail_fence_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_plaintext)

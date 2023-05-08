def caesar_cipher(plaintext, key, mode):
    plaintext = plaintext.upper()
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if mode == "encrypt":
                shifted = (ord(char) - 65 + key) % 26
            elif mode == "decrypt":
                shifted = (ord(char) - 65 - key) % 26
            ciphertext += chr(shifted + 65)
        else:
            ciphertext += char
    return ciphertext


plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))

# Encrypt
ciphertext = caesar_cipher(plaintext, key, "encrypt")
print("Encrypted ciphertext:", ciphertext)

# Decrypt
decrypted = caesar_cipher(ciphertext, key, "decrypt")
print("Decrypted plaintext:", decrypted)

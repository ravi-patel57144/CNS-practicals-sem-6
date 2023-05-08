def monoalphabetic_cipher(plaintext, key, mode):
    key_map = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", key))
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            if mode == "encrypt":
                ciphertext += key_map[char]
            elif mode == "decrypt":
                inverted_key_map = {v: k for k, v in key_map.items()}
                ciphertext += inverted_key_map[char]
        else:
            ciphertext += char
    return ciphertext

key = "KDIJXBVTZLSWYGAHNUPOMCQERF"

plaintext = input("Enter plaintext: ")

ciphertext = monoalphabetic_cipher(plaintext, key, "encrypt")
print("Encrypted ciphertext:", ciphertext)

decrypted = monoalphabetic_cipher(ciphertext, key, "decrypt")
print("Decrypted plaintext:", decrypted)

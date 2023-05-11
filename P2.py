def generate_monoalphabetic_key():
    import random
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)
    key = dict(zip('abcdefghijklmnopqrstuvwxyz', alphabet))
    return key


def monoalphabetic_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += key[char.lower()].upper()
            else:
                encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text


def monoalphabetic_decrypt(encrypted_text, key):
    decrypted_text = ""
    reverse_key = {v: k for k, v in key.items()}
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += reverse_key[char.lower()].upper()
            else:
                decrypted_text += reverse_key[char]
        else:
            decrypted_text += char
    return decrypted_text


# Plaintext
plaintext = input("Enter Plaintext:")

# Generate a random monoalphabetic key
key = generate_monoalphabetic_key()

encrypted_text = monoalphabetic_encrypt(plaintext, key)
decrypted_text = monoalphabetic_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)

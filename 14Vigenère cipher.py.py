import random

# Function to generate a random key of a given length
def generate_key(length):
    key = [random.randint(0, 25) for i in range(length)]
    return key

# Function to encrypt a message using the one-time pad version of the Vigenère cipher
def encrypt_vigenere_one_time_pad(plaintext, key):
    ciphertext = ""
    key_index = 0
    for c in plaintext.lower():
        if c.isalpha():
            shift = key[key_index]
            ciphertext += chr(((ord(c) - 97 + shift) % 26) + 97)
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += c
    return ciphertext

# Function to decrypt a message using the one-time pad version of the Vigenère cipher
def decrypt_vigenere_one_time_pad(ciphertext, key):
    plaintext = ""
    key_index = 0
    for c in ciphertext.lower():
        if c.isalpha():
            shift = key[key_index]
            plaintext += chr(((ord(c) - 97 - shift) % 26) + 97)
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += c
    return plaintext

# Example usage
plaintext = "meetmeattheusualplaceatteneigh"
key = generate_key(len(plaintext))
ciphertext = encrypt_vigenere_one_time_pad(plaintext, key)
decrypted_plaintext = decrypt_vigenere_one_time_pad(ciphertext, key)

print("Plaintext: " + plaintext)
print("Key: " + " ".join(str(x) for x in key))
print("Ciphertext: " + ciphertext)
print("Decrypted plaintext: " + decrypted_plaintext)

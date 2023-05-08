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
plaintext = "sendmoremoney"
key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
ciphertext = encrypt_vigenere_one_time_pad(plaintext, key)
print("Ciphertext: " + ciphertext)

# Brute force attack to find key
target_plaintext = "cashnotneeded"
target_ciphertext = "slyqaejzjeap"

for i in range(26):
    for j in range(26):
        for k in range(26):
            key = [i, j, k]
            decrypted_plaintext = decrypt_vigenere_one_time_pad(target_ciphertext, key)
            if decrypted_plaintext == target_plaintext:
                print("Key: " + " ".join(str(x) for x in key))
                print("Decrypted plaintext: " + decrypted_plaintext)

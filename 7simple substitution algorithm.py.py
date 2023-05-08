import re

def frequency_analysis(ciphertext):
    """
    Compute the frequency of each letter in the ciphertext.
    """
    freq_dict = {}
    for c in ciphertext:
        if c.isalpha():
            c = c.upper()
            freq_dict[c] = freq_dict.get(c, 0) + 1
    freq_list = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return freq_list

def decrypt_substitution(ciphertext, key):
    """
    Decrypt a ciphertext using a simple substitution cipher with the given key.
    """
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            c = c.upper()
            plaintext += key[c]
        else:
            plaintext += c
    return plaintext

# Example ciphertext
ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"
# Compute the frequency of each letter in the ciphertext
freq_list = frequency_analysis(ciphertext)
# Determine the most frequent letter in the ciphertext
most_frequent = freq_list[0][0]
# Determine the second most frequent letter in the ciphertext
second_most_frequent = freq_list[1][0]
# Determine the shift between the most frequent letter and "E" (the most frequent letter in English)
shift = (ord(most_frequent) - ord('E')) % 26
# Determine the shift between the second most frequent letter and "T" (the second most frequent letter in English)
second_shift = (ord(second_most_frequent) - ord('T')) % 26

# Brute-force search for the key that decrypts the ciphertext
for i in range(26):
    key = {}
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # Compute the index of the character in the alphabet after applying the shift
        idx = (ord(c) - ord('A') + i) % 26
        # Map the character to the decrypted character using the key
        key[c] = chr(idx + ord('A'))
    # Decrypt the ciphertext using the key
    plaintext = decrypt_substitution(ciphertext, key)
    # Check if the decrypted plaintext contains English words
    if re.search(r'\b(the|and|of|to)\b', plaintext, re.IGNORECASE):
        # Print the decrypted plaintext and the key used to decrypt it
        print(f"Key: {key}")
        print(plaintext)

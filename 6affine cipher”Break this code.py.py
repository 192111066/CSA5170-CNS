def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Compute the modular inverse of a modulo m, if it exists.
    """
    for i in range(1, m):
        if (a*i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    """
    Decrypt a ciphertext using an affine cipher with parameters a and b.
    """
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    for c in ciphertext:
        if c.isalpha():
            # Convert the character to a number (A=0, B=1, ..., Z=25)
            c_num = ord(c.upper()) - ord('A')
            # Decrypt the character using the affine cipher
            p_num = (a_inv * (c_num - b)) % 26
            # Convert the number back to a character and append to the plaintext
            plaintext += chr(p_num + ord('A'))
        else:
            # Non-alphabetic characters are left as-is
            plaintext += c
    return plaintext

# Example ciphertext
ciphertext = "BUBQDQDYJXJSDXYBQWJI"
# Most frequent letter is "B"
most_frequent = "B"
# Second most frequent letter is "U"
second_most_frequent = "U"

# Determine the shift between the most frequent letter and "E" (the most frequent letter in English)
shift = (ord(most_frequent) - ord('E')) % 26
# Determine the shift between the second most frequent letter and "T" (the second most frequent letter in English)
second_shift = (ord(second_most_frequent) - ord('T')) % 26

# Brute-force search for the values of a and b that decrypt the ciphertext
for a in range(1, 26):
    # Check if a is allowed in the affine cipher
    if gcd(a, 26) != 1:
        continue
    for b in range(26):
        # Decrypt the ciphertext using the affine cipher with parameters a and b
        plaintext = affine_decrypt(ciphertext, a, b)
        # Count the occurrences of the most frequent and second most frequent letters in the decrypted plaintext
        freq_dict = {}
        for c in plaintext:
            if c.isalpha():
                c = c.upper()
                freq_dict[c] = freq_dict.get(c, 0) + 1
        freq_list = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        if freq_list[0][0] == most_frequent and freq_list[1][0] == second_most_frequent:
            # Print the decrypted plaintext and the parameters used to decrypt it
            print(f"a = {a}, b = {b}: {plaintext}")

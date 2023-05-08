# Function to perform a letter frequency attack on an additive cipher
def letter_frequency_attack(ciphertext, num_plaintexts=10):
    # Compute the frequency of each letter in the ciphertext
    freq = {}
    for c in ciphertext.lower():
        if c.isalpha():
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

    # Sort the letters in descending order of frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Compute the most likely shift for each letter in the ciphertext
    most_likely_shifts = {}
    for c in sorted_freq:
        shift = (ord(c[0]) - ord('e')) % 26
        most_likely_shifts[c[0]] = shift

    # Use the most likely shifts to decrypt the ciphertext
    plaintexts = []
    for i in range(26):
        plaintext = ""
        for c in ciphertext.lower():
            if c.isalpha():
                plaintext += chr(((ord(c) - 97 - most_likely_shifts[c]) % 26) + 97)
            else:
                plaintext += c
        plaintexts.append(plaintext)
        most_likely_shifts = {k: (v + 1) % 26 for k, v in most_likely_shifts.items()}

    # Sort the plaintexts by frequency of English letters (E, T, A, O, I, N)
    def score_plaintext(plaintext):
        score = 0
        for c in plaintext.lower():
            if c in "etaoin":
                score += 1
        return score

    plaintexts = sorted(plaintexts, key=score_plaintext, reverse=True)

    # Return the top num_plaintexts plaintexts
    return plaintexts[:num_plaintexts]

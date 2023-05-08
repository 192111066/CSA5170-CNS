import string

# English letter frequency table
FREQ_TABLE = {
    'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425,
    'e': 0.1270, 'f': 0.0223, 'g': 0.0202, 'h': 0.0609,
    'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
    'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193,
    'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
    'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
    'y': 0.0197, 'z': 0.0007
}

def get_cipher_text():
    # Ask user to input the cipher text
    cipher_text = input("Enter the cipher text: ")
    return cipher_text.lower()

def calc_letter_freq(cipher_text):
    # Calculate letter frequency in the cipher text
    letter_freq = {}
    for letter in string.ascii_lowercase:
        letter_freq[letter] = 0
    for letter in cipher_text:
        if letter in letter_freq:
            letter_freq[letter] += 1
    return letter_freq

def calc_score(plain_text):
    # Calculate the score for the plain text
    score = 0
    for letter in plain_text:
        if letter in FREQ_TABLE:
            score += FREQ_TABLE[letter]
    return score

def decrypt(cipher_text, key):
    # Decrypt the cipher text using the key
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            plain_text += key[letter]
        else:
            plain_text += letter
    return plain_text

def find_possible_keys(cipher_text, letter_freq):
    # Find the possible keys
    possible_keys = []
    for i in range(26):
        key = {}
        for letter in string.ascii_lowercase:
            new_letter = chr(((ord(letter) - 97 + i) % 26) + 97)
            key[new_letter] = letter
        possible_plain_text = decrypt(cipher_text, key)
        score = calc_score(possible_plain_text)
        possible_keys.append((key, score))
    # Sort the possible keys by their score
    possible_keys.sort(key=lambda x: x[1], reverse=True)
    return possible_keys

def display_top_10_plain_text(possible_keys):
    # Display the top 10 possible plain text
    print("Top 10 possible plaintexts:")
    for i in range(min(10, len(possible_keys))):
        key, score = possible_keys[i]
        plain_text = decrypt(cipher_text, key)
        print("Key: ", key)
        print("Score: ", score)
        print("Plain text: ", plain_text)
        print()

def main():
    # Get the cipher text and calculate letter frequency
    cipher_text = get_cipher_text()
    letter_freq = calc_letter_freq(cipher_text)
    # Find the possible keys
    possible_keys

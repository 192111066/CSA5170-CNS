import string

def generate_cipher(keyword):
    """Generate the cipher sequence based on the given keyword"""
    keyword = keyword.upper()
    alphabet = string.ascii_uppercase
    unused_letters = ''.join([c for c in alphabet if c not in keyword])
    cipher = keyword + unused_letters
    return cipher

def encrypt(plaintext, keyword):
    """Encrypt the plaintext using the monoalphabetic cipher"""
    cipher = generate_cipher(keyword)
    plaintext = plaintext.upper()
    ciphertext = ''
    for c in plaintext:
        if c in string.ascii_uppercase:
            index = string.ascii_uppercase.index(c)
            ciphertext += cipher[index]
        else:
            ciphertext += c
    return ciphertext

def decrypt(ciphertext, keyword):
    """Decrypt the ciphertext using the monoalphabetic cipher"""
    cipher = generate_cipher(keyword)
    plaintext = ''
    for c in ciphertext:
        if c in string.ascii_uppercase:
            index = cipher.index(c)
            plaintext += string.ascii_uppercase[index]
        else:
            plaintext += c
    return plaintext

# Example usage
plaintext = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
keyword = 'CIPHER'
ciphertext = encrypt(plaintext, keyword)
print(ciphertext)
decrypted_plaintext = decrypt(ciphertext, keyword)
print(decrypted_plaintext)

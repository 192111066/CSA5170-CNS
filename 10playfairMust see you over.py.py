def prepare_input(text):
    # This function prepares the plaintext by converting it to uppercase
    # and replacing J with I, since I and J are typically treated as the same letter
    text = text.upper().replace('J', 'I')
    # Split the plaintext into pairs of letters
    pairs = []
    i = 0
    while i < len(text):
        # If the last pair has only one letter, add an X to make it a pair
        if i == len(text) - 1:
            pairs.append((text[i], 'X'))
            i += 1
        # If the two letters are the same, add an X between them
        elif text[i] == text[i+1]:
            pairs.append((text[i], 'X'))
            i += 1
        else:
            pairs.append((text[i], text[i+1]))
            i += 2
    return pairs

def create_playfair_matrix(key):
    # This function creates the Playfair matrix based on the given keyword
    # First, remove any duplicate letters from the keyword and convert it to uppercase
    key = ''.join(dict.fromkeys(key.upper()))
    # Add the remaining letters of the alphabet to the keyword to create the matrix
    matrix = key
    for letter in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if letter not in matrix:
            matrix += letter
    # Reshape the matrix into a 5x5 array
    matrix = [list(matrix[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, letter):
    # This function finds the position of a given letter in the matrix
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return (i, j)

def encrypt_playfair(plaintext, key):
    # First, prepare the plaintext and create the Playfair matrix
    pairs = prepare_input(plaintext)
    matrix = create_playfair_matrix(key)
    # For each pair of letters in the plaintext, encrypt them using the Playfair rules
    ciphertext = ''
    for pair in pairs:
        # Find the positions of the two letters in the matrix
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])
        # If the letters are in the same row, replace them with the letters to their right
        if row1 == row2:
            ciphertext += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        # If the letters are in the same column, replace them with the letters below them
        elif col1 == col2:
            ciphertext += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        # Otherwise, replace the letters with the letters in the same row but in the other column
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

# Example usage:
plaintext = 'Must see you over Cadogan West. Coming at once'
key = 'CIPHER'
ciphertext = encrypt_playfair(plaintext, key)
print(ciphertext)

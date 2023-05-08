import numpy as np

# Define the key matrix
key = np.array([[9, 4], [5, 7]])

# Define the message to be encrypted
message = "meet me at the usual place at ten rather than eight oclock"

# Convert the message to numerical form
numerical_message = [ord(c) - ord('a') for c in message.lower() if c.isalpha()]

# Pad the message with 'x' if its length is odd
if len(numerical_message) % 2 == 1:
    numerical_message.append(ord('x') - ord('a'))

# Divide the numerical message into groups of two
groups = np.array(numerical_message).reshape(-1, 2)

# Perform matrix multiplication with the key
encrypted_groups = np.dot(groups, key) % 26

# Convert the encrypted numerical values back to letters
encrypted_message = "".join([chr(c + ord('a')) for c in encrypted_groups.flatten()])

print(encrypted_message)

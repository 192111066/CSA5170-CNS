# Define the inverse of the key matrix
inv_key = np.linalg.inv(key)
det_key = int(round(np.linalg.det(key)))
inv_det_key = pow(det_key, -1, 26)
inv_key = np.round((inv_key * det_key * inv_det_key) % 26).astype(int)

# Define the ciphertext to be decrypted
ciphertext = "ctilhbswzayxmyyvfuliloylshthfcjqpzx"

# Convert the ciphertext to numerical form
numerical_ciphertext = [ord(c) - ord('a') for c in ciphertext]

# Divide the numerical ciphertext into groups of two
groups = np.array(numerical_ciphertext).reshape(-1, 2)

# Perform matrix multiplication with the inverse of the key
decrypted_groups = np.dot(groups, inv_key) % 26

# Convert the decrypted numerical values back to letters
decrypted_message = "".join([chr(c + ord('a')) for c in decrypted_groups.flatten()])

print(decrypted_message)

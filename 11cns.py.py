import itertools

def generate_keys():
    # Create a list of all letters in the alphabet, except for "j"
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    # Generate all possible permutations of the alphabet
    permutations = itertools.permutations(alphabet, 25)
    # Loop through all permutations and yield each one as a 5x5 grid
    for p in permutations:
        key = [list(p[i:i+5]) for i in range(0, 25, 5)]
        yield key
num_keys = len(list(itertools.permutations("abcdefghiklmnopqrstuvwxyz", 25)))
print(f"Number of possible keys: {num_keys}")
# Total number of permutations
total_permutations = num_keys

# Number of permutations that produce the same encryption results due to reflection
reflected_permutations = num_keys // 2

# Number of permutations that produce the same encryption results due to rotation
rotated_permutations = num_keys // 4

# Effective number of unique keys
unique_keys = total_permutations // (reflected_permutations * rotated_permutations)

print(f"Number of effectively unique keys: {unique_keys}")

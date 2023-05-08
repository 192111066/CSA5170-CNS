def gcd(a, b):
    """
    Compute the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def is_allowed(a):
    """
    Determine if the value of a is allowed in the affine Caesar cipher.
    """
    return gcd(a, 26) == 1

# Test the function with some example values of a
for a in range(1, 26):
    if is_allowed(a):
        print(f"a = {a} is allowed")
    else:
        print(f"a = {a} is not allowed")

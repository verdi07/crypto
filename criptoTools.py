# Tools to code our messages

# Gets the maximum common divisor
def mcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def invMod(a, m):
    # Gets the modular inverse of a mod m
    # number x which a * x mod x = 1

    if mcd(a, m) != 1:
        # a and m are not coprimes, inverse module does not exist
        return None

    # Euclides extended algorythm
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

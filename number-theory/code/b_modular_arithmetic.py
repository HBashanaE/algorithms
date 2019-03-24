import math

def modular_exponentiation(num, power, mod):
    """Returns a**b mod m faster
    Time Complexity : O(log n)"""

    res = 1
    num %= mod
    while power > 0:
        if (power % 2) == 1:
            res = (res * num) % mod
        power //= 2
        num = (num * num) % mod
    return res


def modular_inverse(num, P):
    """Returns modular inverse of num iff P is prime
    If a and m are relatively prime, then modulo inverse is a^(m-2) mod m 

    If this is used frequently, cache values for better performance
    (if P is const value depend only on num - so can be cached and used easily)
    """

    # Remove if condition if is is sure tha P is a prime
    if math.gcd(num, P) != 1: 
        return -1
    else: 
        return pow(num, P - 2, P)
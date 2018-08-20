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

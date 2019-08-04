def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def _count_co_primes(number):
    if number == 1:
        return 0
    co_primes = 1
    p_i = 2
    while p_i * p_i <= number:
        a_i = 0
        while number % p_i == 0:
            a_i += 1
            number //= p_i
        if a_i > 0:
            co_primes *= pow(p_i, a_i - 1) * (p_i - 1)
        p_i += 1
    if number > 1:
        co_primes *= (number - 1)
    return co_primes


def _general_modular_inverse(n, p):
    phi_n = _count_co_primes(n)
    return pow(n, phi_n-1, p)


def diophantine(a, b, c):
    """Solve equations of type ax + by = c"""
    gcd_a_b = _gcd(a, b)

    if gcd_a_b == 0:
        return None

    def f(x, y, k):
        return (x+(k*b)/gcd_a_b, y-(k*a)/gcd_a_b)

    return f


def chinese_remainder_theorem(n, results, modulars):
    """Solve equations of type:
    x = a1 (mod m1)
    x = a2 (mod m2)
    x = an (mod mn)
    where all pairs of mi are coprime
    """
    multiplication = 1
    for i in range(n):
        multiplication *= modulars[i]

    def Xm_inv(x, m):
        return _general_modular_inverse(x, m)

    def X(k):
        return multiplication//modulars[k]

    x = 0
    for k in range(n):
        Xk = X(k)
        x += results[k]*Xk*Xm_inv(Xk, modulars[k])

    return x


print(chinese_remainder_theorem(3, [3, 4, 2], [5, 7, 3]))

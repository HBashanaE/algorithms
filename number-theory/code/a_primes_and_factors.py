import random


def is_prime(number: int) -> bool:
    """Checks whether a number is prime
    Time Complexity: O(sqrt(n))"""

    if number == 1:
        return False
    root_n = int(number ** 0.5)
    for factor in range(2, root_n + 1):
        if number % factor == 0:
            return False
    return True


def miller_rabin(n, trials=8):
    """
    This is accurate 100% till 341550071728321 (~10^15)
    After that this will fallback to random version with k trials

    This version will give answers with a very small probability of being false. 
    That probability being dependent number of trials (automatically set to 8).

    Time Complexity is O(k lglglgn) where k is number of tests (=8)
    """
    if n == 2 or n == 3:
        return True
    if n == 0 or n == 1 or n % 2 == 0 or n % 3 == 0:
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    if n < 1373653:
        tests = (2, 3)
    elif n < 25326001:
        tests = (2, 3, 5)
    elif n < 118670087467:
        if n == 3215031751:
            return False
        tests = (2, 3, 5, 7)
    elif n < 2152302898747:
        tests = (2, 3, 5, 7, 11)
    elif n < 3474749660383:
        tests = (2, 3, 5, 7, 11, 13)
    elif n < 341550071728321:
        tests = (2, 3, 5, 7, 11, 13, 17)
    else:
        # Fallback
        return not any(trial_composite(random.randrange(2, n)) for _ in range(trials))
    return not any(trial_composite(a) for a in tests)


def prime_factorize(number: int) -> list:
    """Gets all factors of a number
    Time Complexity: O(sqrt(n))"""

    factors = []
    factor = 2
    while factor * factor <= number:
        while number % factor == 0:
            factors.append(factor)
            number //= factor
        factor += 1
    if number > 1:
        factors.append(number)
    return factors


def sieve_of_eratosthenes(max_limit: int) -> list:
    """Builds a sieve which denotes whether a
    number (up to a max_limit) is prime or not
    sieve(n) = 0 denotes that n is prime
    sieve(n) = p denotes that smallest factor to n is p
    sieve[0] = -1 but 0 is not prime
    sieve[1] = -1 but 1 is not prime
    Time Complexity: O(n log log n) ~ O(n)
    However because a array is built this cannot
    process for numbers bigger than 10^5 because of
    memory restrictions"""

    sieve = [0] * (max_limit + 1)
    sieve[0] = -1
    sieve[1] = -1
    for x in range(2, max_limit + 1):
        if sieve[x] != 0:
            continue
        else:
            for i in range(2 * x, max_limit + 1, x):
                sieve[i] = x
    return sieve


def construct_prime_factors(number: int, sieve: list) -> list:
    """Constructs all factors using sieve_of_eratosthenes
    Time Complexity: O(log n)
    However because a array is built this cannot
    process for numbers bigger than 10^5 because of
    memory restrictions
    """

    factors = []
    while sieve[number] >= 2:
        factors.append(sieve[number])
        number //= sieve[number]
    if sieve[number] == 0:
        factors.append(number)
    factors.reverse()
    return factors


def euclid_gcd(a, b):
    """Euclid algorithm to calculate gcd
    Time Complexity: O(log n)
    """

    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Euclid algorithm to calculate lcm
    Time Complexity: O(log n)
    """

    gcd = euclid_gcd(a, b)
    _lcm = (a * b) // gcd
    return _lcm


# Euler Totient Function
def count_co_primes(number: int) -> int:
    """Gets all co primes i of number such as 1<=i<=number
    Time Complexity: O(sqrt(n))"""

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


def general_modular_inverse(n, p):
    """Find Modullar inverse of any number where n and p are coprime
    Time Complexity = sqrt(n)"""
    phi_n = count_co_primes(n)
    return pow(n, phi_n-1, p)
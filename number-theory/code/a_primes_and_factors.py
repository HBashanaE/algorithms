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

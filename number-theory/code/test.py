import unittest

from a_primes_and_factors import *
from b_modular_arithmetic import *


class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(1000000007))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(1689550229929))

    def test_prime_factorize(self):
        self.assertListEqual(prime_factorize(2), [2])
        self.assertListEqual(prime_factorize(5), [5])
        self.assertListEqual(prime_factorize(12), [2, 2, 3])
        self.assertListEqual(prime_factorize(1000000007), [1000000007])
        self.assertListEqual(prime_factorize(1), [])
        self.assertListEqual(prime_factorize(6), [2, 3])
        self.assertListEqual(prime_factorize(100), [2, 2, 5, 5])
        self.assertListEqual(prime_factorize(1689550229929), [1299827, 1299827])

    def test_sieve_of_eratosthenes(self):
        self.assertListEqual(sieve_of_eratosthenes(2), [-1, -1, 0])
        self.assertListEqual(sieve_of_eratosthenes(4), [-1, -1, 0, 0, 2])
        self.assertListEqual(sieve_of_eratosthenes(12), [-1, -1, 0, 0, 2, 0, 3, 0, 2, 3, 5, 0, 3])

    def test_construct_factors(self):
        sieve = sieve_of_eratosthenes(150)
        self.assertListEqual(construct_prime_factors(2, sieve), [2])
        self.assertListEqual(construct_prime_factors(5, sieve), [5])
        self.assertListEqual(construct_prime_factors(12, sieve), [2, 2, 3])
        self.assertListEqual(construct_prime_factors(1, sieve), [])
        self.assertListEqual(construct_prime_factors(6, sieve), [2, 3])
        self.assertListEqual(construct_prime_factors(100, sieve), [2, 2, 5, 5])

    def test_euclid_gcd(self):
        self.assertEqual(euclid_gcd(1, 1), 1)
        self.assertEqual(euclid_gcd(1, 2), 1)
        self.assertEqual(euclid_gcd(100, 100), 100)
        self.assertEqual(euclid_gcd(4400, 264), 88)
        self.assertEqual(euclid_gcd(573147844013817084101, 927372692193078999176), 1)

    def test_lcm(self):
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(100, 100), 100)
        self.assertEqual(lcm(4400, 264), 13200)
        self.assertEqual(lcm(573147844013817084101, 927372692193078999176), 531521659127752446580404735205751701700776)

    def test_count_co_primes(self):
        self.assertEqual(count_co_primes(1), 0)
        self.assertEqual(count_co_primes(12), 4)
        self.assertEqual(count_co_primes(100), 40)
        self.assertEqual(count_co_primes(1000000007), 1000000006)
        self.assertEqual(count_co_primes(57314784401), 49049098560)


class TestModularArithmetic(unittest.TestCase):
    def test_modular_exponentiation(self):
        self.assertEqual(modular_exponentiation(0, 6, 1), 0)
        self.assertEqual(modular_exponentiation(1, 22, 30), 1)
        self.assertEqual(modular_exponentiation(2, 4, 30), 16)
        self.assertEqual(modular_exponentiation(4, 1000, 1000000009), pow(4, 1000, 1000000009))
        self.assertEqual(modular_exponentiation(11, 1689, 1000000009), pow(11, 1689, 1000000009))


if __name__ == '__main__':
    unittest.main()

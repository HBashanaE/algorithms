""" 
When Memory is the issue - However timeout is an issue
Sieve creation for 100000 elements (Olglgn)

              |      TIME                  |       MEM
bitset sieve: |  1.048710823059082s        |           13 360 B = 13KB
list sieve:   |  0.06738710403442383s      |          800 072 B = 800KB
set sieve:    |  0.09641146659851074s      |        4 194 528 B = 4MB
"""


def bitset():
    return 0


def bitset_add(bitset, number):
    return bitset | (1 << number)


def bitset_remove(bitset, number):
    return bitset ^ (1 << number)


def bitset_exists(bitset, number):
    return bitset & (1 << number)


def bitset_to_set(bitset):
    elems = set()
    i = 0
    while bitset:
        if bitset & 1:
            elems.add(i)
        bitset = bitset >> 1
        i += 1
    return elems


if __name__ == "__main__":
    # -------------------------------------------------
    import os
    import time
    import sys

    os.system('clear')
    max_limit = 100000

    bs_a = time.time()
    sieve = bitset()
    sieve = bitset_add(sieve, 0)
    sieve = bitset_add(sieve, 1)

    for x in range(2, max_limit + 1):
        if bitset_exists(sieve, x):
            continue
        else:
            for i in range(2 * x, max_limit + 1, x):
                sieve = bitset_add(sieve, i)
    bs_b = time.time()

    print("bitset sieve: {}s \t|\t {}B".format(
        bs_b - bs_a, sys.getsizeof(sieve)))
    # print(no_primes)
    # -------------------------------------------------

    l_a = time.time()
    sieve_lst = [0] * (max_limit + 1)
    sieve_lst[0] = -1
    sieve_lst[1] = -1
    for x in range(2, max_limit + 1):
        if sieve_lst[x] != 0:
            continue
        else:
            for i in range(2 * x, max_limit + 1, x):
                sieve_lst[i] = 1
    l_b = time.time()

    print("list sieve: {}s \t|\t {}B".format(
        l_b - l_a, sys.getsizeof(sieve_lst)))

    # --------------------------------------------------

    s_a = time.time()
    sieve_set = set()
    sieve_set.add(0)
    sieve_set.add(0)
    for x in range(2, max_limit + 1):
        if x in sieve_set:
            continue
        else:
            for i in range(2 * x, max_limit + 1, x):
                sieve_set.add(i)
    s_b = time.time()

    print("set sieve: {}s \t|\t {}B".format(
        s_b - s_a, sys.getsizeof(sieve_set)))

    # --------------------------------------------------------------

    assert (bitset_to_set(sieve) == {
            i for i in range(max_limit + 1) if sieve_lst[i]})

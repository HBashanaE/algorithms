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

    print("bitset sieve: {}s \t|\t {}B".format(bs_b - bs_a, sys.getsizeof(sieve)))
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

    print("list sieve: {}s \t|\t {}B".format(l_b - l_a, sys.getsizeof(sieve_lst)))
        
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

    print("set sieve: {}s \t|\t {}B".format(s_b - s_a, sys.getsizeof(sieve_set)))

    # --------------------------------------------------------------

    assert (bitset_to_set(sieve) == {
            i for i in range(max_limit + 1) if sieve_lst[i]})

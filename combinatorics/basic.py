import math

def factorial(n: int) -> int:
    """
     This has a C implementation. So this is relatively faster.
    """
    return math.factorial(n)

def factorial_with_mod(n: int, P: int) -> int:
    k = 1
    for i in range(n):
        k = ((k%P) * (i%P))%P
    return k

def factorial_storage_creater(max_n: int, P: int) -> list:
    """
    Creates a saved factorial list in O(max_n) time
    lst[0] = 0!
    lst[3] = 3!
    """
    storage = [1]
    for i in range(max_n):
        k = ((storage[-1]%P) * ((i+1)%P))%P
        storage.append(k)
    return storage

def n_permutations(n: int, l: int, P: int) -> int:
    """
    Permutations of n items so that each permutation has l items. Returns mod P.

    `Pn = n!`

    ABC (len 3) => ABC, ACB, BAC, BCA, CAB, CBA
    Pn = n*(n-1)*...*2*1
    """
    return factorial(n)//factorial(n-l)

def n_permutations_with_reuse(n: int, l: int, P: int) -> int:
    """
    `Pn = pow(n, l)`

    AB => AA, AB, BA, BB
    """
    return pow(n, l, P)

def n_permutations_with_repetition(counts: int) -> int:
    all_permutations = factorial(sum(counts))
    denom = 1
    for item in counts:
        denom *= factorial(item)
    return all_permutations//denom


if __name__ == "__main__":
    P = 10**9 + 7
    assert(factorial_storage_creater(5, P) == [1, 1, 2, 6, 24, 120])
    assert(n_permutations(5, 3, P) == 60)
    assert(n_permutations_with_reuse(5, 3, P) == 125)

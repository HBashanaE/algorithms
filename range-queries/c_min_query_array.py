from collections import defaultdict
import random


def generate_min_query_array(arr):
    """
    Min Query Array Generator: O(nlgn)

    Benchmark
    for arr = [i for i in range(100000)]
    On Laptop
    PYTHON3: 0.7859153747558594s
    On hackerrank 
    PYTHON3: 2.728243112564087s
    PYPY3: 0.30783510208129883s
    """
    n = len(arr)
    min_query_array = defaultdict(dict)

    query_size = 1
    while query_size <= n:
        for i in range(n - query_size+1):
            a, b = i, i + query_size-1
            if a == b:
                min_query_array[a][b] = arr[a]
            else:
                w = (b - a + 1)//2

                x = min_query_array[a][a + w - 1]
                y = min_query_array[a + w][b]
                if x < y:
                    min_query_array[a][b] = x
                else:
                    min_query_array[a][b] = y
        query_size <<= 1

    return min_query_array


def get_minimum(min_arr, a, b):
    """
    Gets the minimum value between indices a and b
    a MUST BE GREATER THAN b
    * includes both endpoints a and b
    Time complexity: O(1)
    """
    w = b-a+1
    k = 1
    while k*2 <= w:
        k <<= 1
    return min(min_arr[a][a+k-1], min_arr[b-k+1][b])


if __name__ == "__main__":
    P = 10**9
    n = 100
    arr = [random.randrange(0, P) for _ in range(n)]
    min_arr = generate_min_query_array(arr)\

    for i in range(n):
        for j in range(i+1, n):
            assert(min(arr[i:j+1]) == get_minimum(min_arr, i, j))

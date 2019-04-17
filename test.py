import time, random
from collections import defaultdict

def generate_min_query_array(arr, k):
    n = len(arr)
    min_query_array = defaultdict(dict)

    query_size = 1
    while query_size <= n:
        for i in range(n - query_size+1):
            a, b = i, i + query_size-1
            if a == b:
                min_query_array[a][b] = arr[a]
            else:
                w = (b - a + 1)//k

                x = min_query_array[a][a + w - 1]
                y = min_query_array[a + w][b]
                if x < y:
                    min_query_array[a][b] = x
                else:
                    min_query_array[a][b] = y
        query_size *= k

    return min_query_array


def get_minimum(min_arr, a, b):
    w = b-a+1
    k = 1
    while k*2 <= w:
        k <<= 1
    return min(min_arr[a][a+k-1], min_arr[b-k+1][b])


P = 10**9
x = [random.randrange(0, P) for _ in range(100000)]

a = time.time()
generate_min_query_array(x, 3)
b = time.time()

print(b-a)

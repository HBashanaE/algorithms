import functools

def knapsack(weights, need):
    """
    Given a list of weights [ w 1 , w 2 , . . . , w n ], 
    determine whether a sum can be constrcuted

    Possible(k, i) = True if k == 0
    Possible(k, i) = False if k < 0
    Possible(k, i) = False if i == len(weights)
    Possible(k, i) = Possible(k-wi, i+1) || Possible(k, i+1)
    """

    W = len(weights)
    
    @functools.lru_cache(maxsize=1024, typed=False)
    def possible(k, i):
        if k == 0:
            return True
        if k < 0:
            return False
        if i == W:
            return False
        return possible(k-weights[i], i+1) or possible(k, i+1)

    v = possible(need, 0)
    # print(possible.cache_info())
    return v

if __name__ == "__main__":
    x = [1, 3, 3, 4, 5, 5, 6, 6, 3, 3, 3, 3]
    print(knapsack(x, 23))
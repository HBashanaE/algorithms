def min_coins(coin_set, p, solved):
    """Recursive solution with dynamic programing"""
    if p < 0:
        return float("inf")
    elif p == 0:
        return 0
    if p not in solved:
        _min = float("inf")
        for c in coin_set:
            t = min_coins(coin_set, p - c, solved) + 1
            if t < _min:
                _min = t
        solved[p] = _min
    return solved[p]


def min_coins_iter(coin_set, p):
    """Iterative solution with dynamic programming"""
    solved = [0]
    for i in range(1, p + 1):
        _min = 0
        for c in coin_set:
            if i - c >= 0:
                _min = min(solved[i - c], _min) + 1
        solved.append(_min)
    return solved[p]


def min_coins_iter_record(coin_set, p):
    """Iterative solution which records the best solution"""
    solved = [0]
    first_coin_in_best_answer = [0]
    for i in range(1, p + 1):
        _min = float("inf")
        first_coin_in_best_answer.append(0)
        for c in coin_set:
            if i - c >= 0:
                if _min > solved[i - c]:
                    _min = solved[i - c] + 1
                    first_coin_in_best_answer[i] = c
        solved.append(_min)
    i = p
    record = []
    while first_coin_in_best_answer[i] != 0:
        record.append(first_coin_in_best_answer[i])
        i -= first_coin_in_best_answer[i]
    return record


# ---------------------------------
# COINS PROBLEM - ALL SOLUTIONS
# ---------------------------------

def all_ways_to_select_coins(coin_set, p, solved):
    """All solutions to create a sum of money. Recursive."""
    if p < 0:
        return 0
    if p == 0:
        return 1
    if p not in solved:
        _all = 0
        for c in coin_set:
            _all += all_ways_to_select_coins(coin_set, p - c, solved)
        solved[p] = _all
    return solved[p]


print(min_coins([1, 2, 3, 5, 10, 20, 50, 100, 200], 223, {}))
print(min_coins_iter([1, 2, 3, 5, 10, 20, 50, 100, 200], 223))
print(min_coins_iter_record([1, 2, 3, 5, 10, 20, 50, 100, 200], 223))
print(all_ways_to_select_coins([1, 2, 3, 5, 10, 20, 50, 100, 200], 10, {}))
"""
    
    # ---------------------------------
    # LONGEST INCREASING SUBSEQUENCE
    # ---------------------------------
    
    def longest_incr_subs(arr):
        longest = [0] * len(arr)
        for i in range(len(arr)):
            _max = 0
            for j in range(i):
                if arr[j] < arr[i] and _max < longest[j]:
                    _max = longest[j]
            longest[i] = _max + 1
        return max(longest)
    
    
    def longest_incr_subs_nlogn(arr):
        arr.sort()
        longest = [0] * len(arr)
        for i in range(len(arr)):
            _max = 0
            for j in range(i):
                if arr[j] < arr[i] and _max < longest[j]:
                    _max = longest[j]
            longest[i] = _max + 1
        return max(longest)
    
    
    longest_incr_subs_nlogn([6, 2, 5, 1, 7, 4, 8, 3])
    
    
    # ---------------------------------
    # PATHS IN A GRID
    # ---------------------------------
    
    def paths_in_grid(n):
        grid = [[1 if (_c == n - 1 or _r == n - 1) else 0 for _c in range(n)] for _r in range(n)]
        for r in range(n - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
        return grid[0][0]
    
    
    paths_in_grid(70)
"""

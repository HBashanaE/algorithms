# -------------------------------------------------------
# Coin Problem - Find number of minmum coins to make a change
# -------------------------------------------------------


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


# -------------------------------------------------------
# Method to make the change by using minimum number of coins
# -------------------------------------------------------

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


# -------------------------------------------------------
# Number of ways to select coins to make a change
# -------------------------------------------------------

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


if __name__ == "__main__":
    print(min_coins([1, 2, 3, 5, 10, 20, 50, 100, 200], 223, {}))
    print(min_coins_iter([1, 2, 3, 5, 10, 20, 50, 100, 200], 223))
    print(min_coins_iter_record([1, 2, 3, 5, 10, 20, 50, 100, 200], 223))
    print(all_ways_to_select_coins([1, 2, 3, 5, 10, 20, 50, 100, 200], 10, {}))

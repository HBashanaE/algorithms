def maximum_sub_array_sum(arr):
    """For each position find the maximum sum that is possible
    for that position
    That means either 'last_value + this_value' or 'this_value'
    if last_value is positive answer is 'last_value + this_value'
    else 'this_value' is bigger
    Then find the maximum in constructed array
    Time Complexity: O(n)"""

    max_sum_arr = [0]
    for i in range(len(arr)):
        if max_sum_arr[i] > 0:
            max_sum_arr.append(arr[i] + max_sum_arr[i])
        else:
            max_sum_arr.append(arr[i])
    _max = -float("inf")
    for j in range(len(arr)):
        if _max < max_sum_arr[j]:
            _max = max_sum_arr[j]
    return _max

# -------------------------------------------------------
# Longest Increasing  Subsequence
# -------------------------------------------------------


def longest_increasing_subsequence(arr):
    """ 
    Find maximum increasing subsquence(not continous)
    O(nlgn)
    """

    arr.sort()
    longest = [0] * len(arr)
    for i in range(len(arr)):
        _max = 0
        for j in range(i):
            if arr[j] < arr[i] and _max < longest[j]:
                _max = longest[j]
        longest[i] = _max + 1
    return max(longest)

# -------------------------------------------------------
# PATHS IN A GRID
# -------------------------------------------------------


def paths_in_grid(n):
    """
    Find paths in a grid
    O(n**2)
    """
    grid = [[1 if (_c == n - 1 or _r == n - 1) else 0 for _c in range(n)]
            for _r in range(n)]
    for r in range(n - 2, -1, -1):
        for c in range(n - 2, -1, -1):
            grid[r][c] = grid[r + 1][c] + grid[r][c + 1]
    return grid[0][0]

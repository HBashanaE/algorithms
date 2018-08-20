def binary_search_recur(arr, find, start, end):
    """Recursive algorithm. Halves search"""
    if start == end:
        return False
    mid = (start + end) // 2
    if arr[mid] == find:
        return True
    elif arr[mid] > find:
        return binary_search_recur(arr, find, start, mid)
    else:
        return binary_search_recur(arr, find, mid + 1, end)


def binary_search_iter(arr, find, start, end):
    """Iterative algorithm. Halves search"""
    while start != end:
        mid = (start + end) // 2
        if arr[mid] == find:
            return True
        elif arr[mid] > find:
            end = mid
        else:
            start = mid + 1
    return False


def binary_search_jump(arr, find):
    """Alternative iterative algorithm. Jump forward and search"""
    jump = len(arr) // 2
    index = 0
    while arr[index] != find:
        while index + jump >= len(arr) or arr[index + jump] > find:
            jump //= 2
            if jump == 0:
                return False
        index += jump
    return True

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

def find_changing_point(func, start, max_range):
    """
    Function to find a value for which a given function changes
    from False to True
    max_range is not important but it is the
    maximum jump length
    So it has to be higher than turning point
    to be efficient
    """

    val = start
    # Initial jump is total length
    jump = max_range
    # Continue until jump is a positive integer
    # ..or there is something to jump
    while jump != 0:
        # If at value this hopes to jump,
        # function takes True, then point which is searched
        # is passed. So must not jump.
        while not func(val + jump):
            # If a jump is possible, jump
            val += jump
        jump //= 2
    # This gives last value for which
    # function is False.
    # Answer is the integer after that
    return val + 1


def find_maximum_point(func, start, max_range):
    """
    Adds a internal function so it can be passed
    Finds a maximum point when given a function
    """

    # Add a converting wrapper to make this a
    # True False step function
    def converted_func(x):
        return func(x) > func(x + 1)

    # Pass to above function
    return find_changing_point(converted_func, start, max_range)


def function_change_position(function, initial_jump, minimum_accuracy=1e-6):
    """
    Find position where boolean function changes
    function has to accept a number and return True False
    F F F F F F F T T T T

    Finds larget value where function is False

    Time complexity O(logn)
    """
    x = -1
    b = initial_jump
    while b>=minimum_accuracy:
        while not function(x+b):
            x += b
        b /= 2
    return x

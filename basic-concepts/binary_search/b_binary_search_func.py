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

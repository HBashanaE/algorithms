"""Demonstrating a classic problem that has 3 possible asymptotic times"""


def maximum_sub_array_sum_1(arr):
    """Answer which compares all possible pairs for
    starting point and ending point and
    uses another internal loop to calculate sum
    Time Complexity: O(n^3)"""

    _max = -float("inf")
    for start in range(len(arr)):
        for end in range(start, len(arr)):
            _sum = 0
            for ind in range(start, end + 1):
                _sum += arr[ind]
            if _max < _sum:
                _max = _sum
    return _max


def maximum_sub_array_sum_2(arr):
    """Answer which compares all possible pairs for
        starting point and ending point but
        dynamically calculate sum when start and end changes
        Time Complexity: O(n^2)"""

    _max = -float("inf")
    for start in range(len(arr)):
        sum_till_end = 0
        for end in range(start, len(arr)):
            sum_till_end += arr[end]
            if _max < sum_till_end:
                _max = sum_till_end
    return _max


def maximum_sub_array_sum_3(arr):
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


def sum_array(arr):
    """
    Creates sum array to calculate sum in O(1) time
        [1 2 3 4 5]
    =>  [0 1 3 6 10 15]
    """
    sum_arr = [0]
    for i in range(len(arr)):
        sum_arr.append(sum_arr[i] + arr[i])
    return sum_arr

def get_sum(sum_arr, i, j):
    """
    Gets sum from sum array
    original array => [1 2 3 4 5]
    i = 0    j = 2  => [1 2 3]
    -> sum is 6
    """
    return sum_arr[j+1] - sum_arr[i]

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    s = sum_array(x)
    assert(s == [0, 1, 3, 6, 10, 15])
    v = get_sum(s, 0, 2)
    assert(v == 6)
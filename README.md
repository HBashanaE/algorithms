# Algorithms

## Basic Concepts

### Binary Search

| Algorithm                                                    | Description                                                  | Time Complexity |
| ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- |
| binary_search_recur(arr, find, start, end)                   | Recursive algorithm. Halves search                           | O(nlgn)         |
| binary_search_iter(arr, find, start, end)                    | Iterative algorithm. Halves search                           | O(nlgn)         |
| binary_search_jump(arr, find)                                | Alternative iterative algorithm. Jump forward and search     | O(nlgn)         |
| find_changing_point(func, start, max_range)                  | Function to find a value for which a given function changes from False to True. (function must only accept int) | ~O(nlgn)        |
| find_maximum_point(func, start, max_range)                   | Finds a maximum point when given a function. (function must only accept int) | ~O(lgn)         |
| function_change_position(function, initial_jump, minimum_accuracy=1e-6) | Find position where boolean function change. Function has to accept a number and return True False (F F F F F F F T T T T) | ~O(lgn)         |


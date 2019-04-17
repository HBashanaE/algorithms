def create_sum_grid(r, c, grid):
    """
    Creates sum grid to calculate sum in O(1) time
        [1 1 1] [1 1 1] [1 1 1]
    =>  [0 0 0 0] [0 1 2 3] [0 2 4 6] [0 3 6 9]
    """
    sum_grid = [[0]*(c+1) for _ in range(r+1)]
    for i in range(r):
        for j in range(c):
            sum_grid[i+1][j+1] = sum_grid[i][j+1] + \
                sum_grid[i+1][j] - sum_grid[i][j] + grid[i][j]
    return sum_grid


def get_sum(sum_grid, r1, c1, r2, c2):
    """
    Gets sum from sum grid
    original grid => [1 1 1] [1 1 1] [1 1 1]
    r1 = 0, c1 = 0      r2 = 0, c2 = 0
    -> (0, 0) point => sum is 1
    """
    if r2 < r1 or c2 < c1:
        return 0
    return sum_grid[r2+1][c2+1] - sum_grid[r1][c2+1] - \
        sum_grid[r2+1][c1] + sum_grid[r1][c1]



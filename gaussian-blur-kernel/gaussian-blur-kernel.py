import math

def gaussian_kernel(size: int, sigma: float) -> list:

    weight_mat = [[0.0 for i in range(size)] for j in range(size)]
    c_row, c_col = size//2, size//2
    total = 0.0
    for i in range(size):
        for j in range(size):
            diff_i = c_row - i
            diff_j = c_col - j

            weight_mat[i][j] = math.exp(-1 * (diff_i**2 + diff_j**2)/ (2 * sigma **2))
            total += weight_mat[i][j]


    for i in range(size):
        for j in range(size):
            weight_mat[i][j] /= total
    return weight_mat
    
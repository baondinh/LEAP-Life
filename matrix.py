# Bao Dinh
# LEAP Life Day 1
# PyTest example 2 using matrix multiplier

# From 
def matrix_multiplication(A, B): 
    # Check if matrix dimensions are compatible for multiplication
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B.")

    # Initialize the result matrix with zeros
    rows_A = len(A)
    cols_B = len(B[0])
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

def test_matrix_multiplication():
    assert matrix_multiplication([[2, 4], [1, 3]], [[1, 1], [1, 1]]) == [[1, 1], [1, 1]]


def functionA(a, b): 
    return

assert functionA == 0
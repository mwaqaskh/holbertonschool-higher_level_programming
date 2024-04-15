#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    squared_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row to store the squared values for the current row
        squared_row = []
        # Iterate over each element in the current row
        for num in row:
            # Compute the square of the current element and append it to the squared row
            squared_row.append(num ** 2)
        # Append the squared row to the squared matrix
        squared_matrix.append(squared_row)

    return squared_matrix

# Example usage:
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = square_matrix_simple(input_matrix)
print(result)

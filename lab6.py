"""
Module for sorting rows of a matrix, calculating column-wise arithmetic means,
and determining the geometric mean of these averages.
"""

def exchange_sort_descending(single_row):
    """
    Sorts a row in descending order using the exchange sort method.
    
    Args:
        single_row (list): A list of numeric values to be sorted.
    
    Returns:
        list: The sorted row in descending order.
    """
    n = len(single_row)
    for i in range(1, n):
        j = i
        while j > 0 and single_row[j] > single_row[j - 1]:
            single_row[j], single_row[j - 1] = single_row[j - 1], single_row[j]
            j -= 1
    return single_row


def calculate_column_arithmetic_mean(input_matrix):
    """
    Calculates the arithmetic mean of each column in a matrix.
    
    Args:
        input_matrix (list of lists): A 2D list representing the matrix.
    
    Returns:
        list: A list of arithmetic means for each column.
    """
    rows = len(input_matrix)
    cols = len(input_matrix[0])
    col_means = []
    for col in range(cols):
        col_sum = 0
        for r in range(rows):
            col_sum += input_matrix[r][col]
        col_means.append(col_sum / rows)
    return col_means


def calculate_geometric_mean(values_list):
    """
    Calculates the geometric mean of a list of values.
    
    Args:
        values_list (list): A list of numeric values.
    
    Returns:
        float: The geometric mean of the values.
    """
    product = 1
    for value in values_list:
        product *= value
    geometric_mean_result = product ** (1 / len(values_list))
    return geometric_mean_result


# Input matrix
original_matrix = [
    [30, 31, 36, 63, -2],
    [2, 24, -3, -7, -1],
    [45, 28, -98, 2, -8],
    [0, -1, -2, -3, 93],
    [11, 10, 72, 85, 66]
]

# Sort each row in descending order
sorted_matrix = [exchange_sort_descending(row[:]) for row in original_matrix]

# Calculate arithmetic means of columns
column_means = calculate_column_arithmetic_mean(sorted_matrix)

# Calculate geometric mean of arithmetic means
geom_mean = calculate_geometric_mean(column_means)

# Display results
print("Original matrix:")
for row in original_matrix:
    print(row)

print("Sorted matrix:")
for row in sorted_matrix:
    print(row)

print(f"Arithmetic means of columns: {column_means}")
print(f"Geometric mean of arithmetic means: {geom_mean}")

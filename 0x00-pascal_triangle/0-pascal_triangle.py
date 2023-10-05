#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""

def pascal_triangle(n):
    """Returns a list of lists of numbers representing the Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Start and end each row with 1
        new_row = [1]

        # Calculate the middle values based on the previous row
        for j in range(1, i):
            new_row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End the row with 1
        new_row.append(1)

        triangle.append(new_row)

    return triangle


#!/usr/bin/env python3
def pascal_triangle(n: int) -> list:
    """
    Generate Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) < n:
        last_row = triangle[-1]
        # Using a list comprehension to generate the next row
        next_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(next_row)

    return triangle

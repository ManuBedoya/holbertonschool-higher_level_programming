#!/usr/bin/python3
"""Module have the matrix_divided to dived a matrix
"""
def matrix_divided(matrix, div):
    """This is the matrix_divided function
    Args:
      matrix (list): List of numbers
      div (int/float): divisor number
    Returns:
       New list with the results
    """
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    result = []
    size_row = len(matrix[0])
    for row in range(len(matrix)):
        result.append([])
        if size_row == len(matrix[row]):
            for item in matrix[row]:
                if type(item) == int or type(item) == float:
                    result[row].append(round(item / div, 2))
                else:
                    raise TypeError('matrix must be a matrix (list of lists) \
                    of integers/floats')
            return result
        else:
            raise TypeError('Each row of the matrix must have the same size')

#!/usr/bin/python3
def pascal_triangle(n):
    list_triangle = []
    if n <= 0:
        return list_triangle
    else:
        list_triangle.append([1])
        if n == 1:
            return list_triangle
        elif n == 2:
            list_triangle.append([1, 1])
            return list_triangle
        else:
            list_triangle.append([1, 1])
            it_col = 3
            list_aux = []
            for row in range(2, n):
                for col in range(it_col):
                    if col == 0 or col == it_col - 1:
                        list_aux.append(1)
                    else:
                        list_aux.append(list_triangle[row - 1][col - 1] +
                                        list_triangle[row - 1][col])
                list_triangle.append(list_aux)
                list_aux = []
                it_col += 1
            return list_triangle

#!/usr/bin/python3
def pascal_triangle(n):
    result = []
    for i in range(n):
        temp = [1]
        for j in range(1, i):
            temp.append(result[-1][j - 1] + result[-1][j])
        if i > 0:
            temp.append(1)
        result.append(temp)
    return result

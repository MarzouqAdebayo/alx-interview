#!/usr/bin/python3
def pascal_triangle(n):
    result = []
    for i in range(n):
        temp = []
        for j in range(i):
            if j == 0:
                temp.append(1)
            else:
                temp.append(result[-1][j - 1] + result[-1][j])
        temp.append(1)
        result.append(temp)
    return result

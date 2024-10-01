#!/usr/bin/python3
def pascal(n):
    line = [1]
    for k in range(n):
        print(line[k], n - k, k + 1)
        res = int((line[k] * (n - k) / (k + 1)))
        print(res)
        line.append(int((line[k] * (n - k) / (k + 1))))
    return line


print(pascal(6))

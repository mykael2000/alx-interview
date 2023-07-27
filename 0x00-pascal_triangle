#!/usr/bin/python3
'''Pascal's Triangle in a module
'''


def pascal_triangle(n):
    '''List of integers representing the Pascals triangle
    '''
    task = []
    if type(n) is not int or n <= 0:
        return task
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(task[i - 1][j - 1] + task[i - 1][j])
        task.append(line)
    return task

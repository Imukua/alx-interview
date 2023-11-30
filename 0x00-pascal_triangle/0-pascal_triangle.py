#!/usr/bin/python3
"""Obtain pascal's triangle for any number"""


def pascal_triangle(n):
    """
    args:: n(int) - number to get pascals triangle
    return:: 
            - list of lists of integers representing the Pascal’s triangle of n
            - empty iff n <= zero
    """
    ptriangle = []

    if n <= 0:
        return ptriangle
    for i in range(n):
        temp = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(ptriangle[i-1][j-1] + ptriangle[i-1][j])
        ptriangle.append(temp)
    return ptriangle
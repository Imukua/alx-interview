#!/usr/bin/python3
""" 0-minoperations- alx-interview"""


def minOperations(n):
    """
    minOperations
    return least no  of operations needed to result in exactly n H characters
    """
    if (n < 2):
        return 0
    ops = 0
    root = 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n / root
            root -= 1
        root += 1
    return ops

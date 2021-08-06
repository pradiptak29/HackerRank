#!/bin/python3

from math import *
import os
import random
import re
import sys


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    res = [None] * 500
    # Initialize result
    res[0] = 1
    res_size = 1

    # Apply simple factorial formula
    # n! = 1 * 2 * 3 * 4...*n
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1

    i = res_size - 1
    while i >= 0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i = i - 1


def multiply(x, res, res_size):
    carry = 0  # Initialize carry

    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10
        # 'prod' in res[]
        # make sure floor division is used
        carry = prod // 10
        i = i + 1

    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1

    return res_size


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

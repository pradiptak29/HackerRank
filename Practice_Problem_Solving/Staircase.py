#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
        print((n - i) * " " + i * "#")

    # print("\n\n\n")
    #
    # for j in range(1, n+1):
    #     print(j*"#")
    #
    # print("\n\n\n")
    #
    # for k in range(1, n+1):
    #     print(((n-k)//2) * " " + k * "#" + ((n-k)//2) * " ")


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

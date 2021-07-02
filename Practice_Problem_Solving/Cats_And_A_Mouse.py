#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if x>z:
        xz_diff = x-z
    else:
        xz_diff = z-x

    if y>z:
        yz_diff = y-z
    else:
        yz_diff = z-y

    if xz_diff<yz_diff:
        return "Cat A"
    elif yz_diff<xz_diff:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        print(result)
        # fptr.write(result + '\n')

    # fptr.close()

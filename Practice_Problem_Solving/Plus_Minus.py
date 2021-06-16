#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, n):
    # Write your code here
    pos = 0
    neg = 0
    zer = 0
    for i in range(0, n):
        if arr[i]>0:
            pos += 1
        elif arr[i] == 0:
            zer += 1
        else:
            neg += 1

    print("{:06f}".format(pos/n))
    print("{:06f}".format(neg/n))
    print("{:06f}".format(zer/n))


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr, n)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    res = []
    for j in range(len(arr)):
        temp = sum - arr[j]
        res.append(temp)

    print(sorted(res)[0], sorted(res)[-1])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

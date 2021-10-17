#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    out = []
    while arr:
        out.append(len(arr))
        arr_min = min(arr)
        arr = list(map(lambda x: x - arr_min, arr))
        arr = list(filter(lambda x: x > 0, arr))

    return out


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(a, b):
    sum = 0
    for i in range(0, a):
        sum += b[i]
    return sum
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar_count, ar)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

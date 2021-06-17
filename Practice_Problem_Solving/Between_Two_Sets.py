#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    max_A = max(a)
    min_B = min(b)

    counter = 0

    for num in range(max_A, min_B + 1):
        l = all([num % numA == 0 for numA in a])
        r = all([numB % num == 0 for numB in b])
        counter += l * r

    return counter


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)
    # fptr.write(str(total) + '\n'
    # fptr.close()

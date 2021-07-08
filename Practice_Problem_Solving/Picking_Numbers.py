#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    b = sorted(a)
    # print(b)
    maximum = 0
    for i in range(len(b)):
        counter = 0
        for j in range(i, len(b)):
            if abs(b[i] - b[j]) > 1:
                break
            counter += 1
            maximum = max(maximum, counter)


    return maximum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

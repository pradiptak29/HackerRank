#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    # count = 0
    # arr = []
    # if n % len(s) == 0:
    #     val = n // len(s)
    # else:
    #     val = n // len(s) + 1
    #
    # for i in range(0, val):
    #     for j in range(len(s)):
    #         arr.append(s[j])
    #
    # arr1 = arr[:n]
    # for i in range(len(arr1)):
    #     if arr1[i] == 'a':
    #         count += 1
    #
    # return count

    half1 = s.count("a") * (n // len(s))
    half2 = s[:n % len(s)].count("a")
    return half1 + half2


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()

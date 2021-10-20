#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, arr):
    # Write your code here
    var = [0] * k
    for x in arr:
        var[x % k] += 1

    answer = min(1, var[0])
    for m in range(1, (k // 2) + 1):
        if m != k - m:
            answer += max(var[m], var[k - m])

    if k % 2 == 0 and var[int(k / 2)] != 0:
        answer += 1

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, s)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()

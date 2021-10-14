#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    count = 0
    ll = len(s)
    while s[:ll] != t[:ll]:
        ll -= 1
        count += 1
    o = ((len(t) - ll) + count)
    if k < o:
        return "No"
    elif (len(s) + len(t)) <= k:
        return "Yes"
    elif 2 * len(t) < k:
        return "Yes"
    elif k % 2 == o % 2:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    t = input()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()

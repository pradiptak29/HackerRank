#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count = Counter(ar)
    # print(count)
    no_of_pairs = 0

    for i in count:
        no_of_pairs += count[i] // 2

    return no_of_pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()

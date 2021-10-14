#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    sum = 0
    numbers1 = []
    for i in range(0, len(queries)):
        start = queries[i][0]
        end = queries[i][1]
        x = queries[i][2]
        print(start, end, x)

    for j in range(start-1, end):
        if numbers[j] == 0:
            sum = sum +

    return sum




if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()


"""
3
5
10
10
1
3
1 2 5
"""
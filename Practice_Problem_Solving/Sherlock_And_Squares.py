#!/bin/python3

import math
import os
import random
import re
import sys
from math import *


#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    count = 0
    count = floor(b ** 0.5) + 1 - ceil(a ** 0.5)
    return count

    # count = 0
    # for i in range(a, b + 1):
    #     root = math.sqrt(i)
    #     if int(root + 0.5) ** 2 == i:
    #         count += 1
    #
    # return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        print(result)
    #     fptr.write(str(result) + '\n')
    # fptr.close()

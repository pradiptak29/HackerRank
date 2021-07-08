#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    answer = []

    for val in range(1, max(p)+1):
        answer.append(p.index(p.index(val)+1)+1)

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    dt = ["".join(sorted(word)) for word in dictionary]
    m = ["".join(sorted(word)) for word in query]
    answer = []
    count_no = Counter(dt)
    for word in m:
        if word in count_no.keys():
            answer.append(count_no[word])
        else:
            answer.append(0)

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())
    dictionary = []
    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)


    query_count = int(input().strip())
    query = []
    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()


"""
Input:-
5
heater
cold
clod
reheat
docl
3
codl
heatre
acdb
"""

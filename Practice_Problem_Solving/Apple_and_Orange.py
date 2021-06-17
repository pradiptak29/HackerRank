#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    # print(s, t, a, b, apples, oranges)
    apple_in_house = []
    orange_in_house = []
    count_apples = 0
    count_oranges = 0

    for i in range(len(apples)):
        x = apples[i] + a
        apple_in_house.append(x)

    for apple in range(len(apple_in_house)):
        if s <= apple_in_house[apple] <= t:
            count_apples += 1

    for j in range(len(oranges)):
        y = oranges[j] + b
        orange_in_house.append(y)

    for orange in range(len(orange_in_house)):
        if s <= orange_in_house[orange] <= t:
            count_oranges += 1


    # print(apple_in_house)
    # print(orange_in_house)
    print(count_apples)
    print(count_oranges)



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)

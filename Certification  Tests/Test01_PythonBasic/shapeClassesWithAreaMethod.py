#!/bin/python3

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, b, l):
        self.b = b
        self.l = l

    def area(self):
        sol = self.b * self.l
        return sol

    pass


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        sol = math.pi * (self.r ** 2)
        return sol
    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        shape_name, params = args[0], tuple(map(int, args[1:]))
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        print(shape.area())
    #     fptr.write("%.2f\n" % shape.area())
    # fptr.close()

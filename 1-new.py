#!/usr/bin/python
import math

max = 1000

def sumDivisibleBy(n):
    p = math.floor((max - 1) / n)
    return math.floor(n * (p * (p + 1)) / 2)

# a or b - (a and b)
print(sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))

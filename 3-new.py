#!/usr/bin/python
import math

num = 600851475143
lastFactor = 1

for i in range(3, int(math.sqrt(num)), 2):
    if num % i == 0:
        lastFactor = i
        num /= i

print(lastFactor)
